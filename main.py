"""
سوف يتم كتابة السورس كود الخاص بالبوت هنا
"""
import time
from user.sessions_time import sessions_time
import db
import markup
import user
import sender
from config import (bot, botName)


# يلتقط الاوامر
@bot.message_handler(commands=["start", "help", "search", 
                                "new_name", "my_name", "kill",
                                    "cancel",])
def command_handler(message):
    chat_id = str(message.chat.id)
    chat_is_private = message.chat.type == "private"
    text = message.text
    # التحقق هل المحادثة خاصة، ام في محادثة عامة
    if chat_is_private:
        # اذا كان النص من هذول الاثنين
        if text.startswith(("/start", "/help")):
            # جلب الرسالة من قاعدة البيانات بعد ازالة ال / للبحث عنه
            msg = db.row("message", "msg", text[1:], "val")
            #  ارسال الرسالة الى المستخدم
            bot.reply_to(message, msg, parse_mode=None if text[1:] == "help" else "markdownv2")
        elif text.startswith("/search"):
            # اذا كان المستخدم موجود في قاعدة البيانات
            if user.found(chat_id):
                if not user.in_sessions(chat_id):
                    if not user.waiting(chat_id):
                        if len(db.column('waiting', 'id')) != 0:
                            user.make_session(chat_id)
                        else:
                            user.add_to_waiting(chat_id)
                            msg = "لقد تم اضافتك الى قائمة الانتظار، عندما يتم ايجاد شخص سوف يتم ارسال رسالة لك\nللالغاء ارسل /cancel"
                            bot.reply_to(message, msg)
                    else:
                        bot.reply_to(message, "انت في قائمة الانتظار حقا\nللالغاء ارسل /cancel")
                else:
                    bot.reply_to(message, "انت في جلسة حقا")
            else:
                # جلب الرسالة من قاعدة البيانات
                msg = db.row("message", "msg", "no_user", "val")
                #  ارسال الرسالة الى المستخدم
                bot.reply_to(message, msg, reply_markup=markup.make_username())
        elif text.startswith("/new_name"):
            user.add_user(chat_id, not chat_id in db.column('users', 'id'))
        elif text.startswith("/my_name"):
            username = user.username(chat_id)
            if username:
                msg = "اسمك الحالي هو: %s\n\nتنويه:\nهذا الاسم سوف يتم عرضه لاي شخص تحادثه عبر البوت" % username
            else:
                msg = "لم يتم انشاء اسم لك بعد.\nلانشاء اسم ارسل /new_name"
            bot.reply_to(message, msg)
        elif text.startswith("/cancel"):
            if user.waiting(chat_id):
                user.del_waiting(chat_id)
                bot.reply_to(message, "لقد تم الغاء البحث عن جلسة بنجاح")
            else:
                bot.reply_to(message, "انت لست بجلسة للبحث عن جلسة ارسل /search")
        elif text.startswith("/kill"):
            if user.in_sessions(chat_id):
                sessions_id = db.row('chat_sessions', 'user_id', chat_id, 'sessions')
                user.delete_sessions(sessions_id, chat_id)
                msg = "لقد تم قطع الجلسة بنجاح\nللبحث عن جلسة اخرى /search"
                bot.reply_to(message, msg)
            else:
                msg = "انت لست في جلسة حقا"
                bot.reply_to(message, msg)
        else:
            pass
    else:
        # جلب الرسالة من قاعدة البيانات
        msg = db.row("message", "msg", "not_private", "val")
        #  ارسال الرسالة الى المستخدم
        bot.reply_to(message, msg)

# يلتقط جميع الرسايل ماعدا الاوامر
@bot.message_handler(func=lambda msg: True, content_types= ["text", "audio", "document", "photo", "sticker",
                                                            "video", "video_note", "voice"])
def message_handler(message):
    chat_id = str(message.chat.id)
    # اذا كان هناك جلسة
    if user.in_sessions(chat_id):
        # ارسال الرسالة الى شريكه في الجلسة اذ لم تنتهي
        if time.time() < float(user.sessions_time(chat_id)):
            sender.send_to_partner(message, chat_id)
        else:
            partner_id =  user.partner(chat_id)
            sessions_id = user.get_sessions(chat_id)
            user.kill_session(sessions_id)
            msg = "لقد انتهى وقت الجلسة، للبحث عن جلسة اخرى /search"
            for u_id in [chat_id, partner_id]:
                bot.send_message(u_id, msg)
    # اذا لم يكن هناك شريك له، سوف يتم تجاهل الرسالة
    else:
        pass

@bot.callback_query_handler(func=lambda call:True)
def query_handler(call):
    callback = call.data
    user_id = str(call.from_user.id)
    # اذا كن الزر المضغوط هو زر اختيار الاسم
    if callback == "username":
        # اذا كان اليوزر ليس موجود في قاعدة البيانات
        if not user.found(user_id):
            user.add_user(user_id, new_user=True)
            bot.delete_message(user_id, call.message.id)
        else:
            # اخباره بأمر تحديث الاسم لان الزر فق للمستخدم الجديد
            bot.send_message(user_id, "لتحديث الاسم المستعار ارسل /new_name")
    else:
        bot.answer_callback_query(call.id, "المرسل %s" % callback)

# تشغيل البوت
while True:
    print(f"Start {botName}")
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except Exception as e:
        print(e)
        time.sleep(10)