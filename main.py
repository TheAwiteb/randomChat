"""
سوف يتم كتابة السورس كود الخاص بالبوت هنا
"""
import time
from telebot import util
import db
import markup
import user
import sender
from config import (bot, botName)


# يلتقط الاوامر
@bot.message_handler(commands=["start", "help", "search", 
                                "new_name", "my_name", "kill",
                                    "cancel","terms_and_conditions",
                                        "privacy_policy",])
def command_handler(message):
    chat_id = str(message.chat.id)
    chat_is_private = message.chat.type == "private"
    text = message.text
    # التحقق هل المحادثة خاصة، ام في محادثة عامة
    if chat_is_private:
        # اذا كان النص من هذول الاثنين
        if text.startswith(("/start", "/help", "/terms_and_conditions",
                                        "/privacy_policy")):
            # ازالة علامة الكوماند
            command = text[1:]
            if command in ["terms_and_conditions", "privacy_policy"]:
                with open(command+'.txt', 'r', encoding="utf-8") as f:
                    for text in util.split_string(f.read(), 3000):
                        bot.reply_to(message, text)
            else:
                # جلب الرسالة من قاعدة البيانات بعد ازالة ال / للبحث عنه
                msg = db.row("message", "msg", command, "val")
                #  ارسال الرسالة الى المستخدم
                bot.reply_to(message, msg)
        elif text.startswith("/search"):
            # اذا كان المستخدم موجود في قاعدة البيانات
            if user.found(chat_id):
                if not user.in_sessions(chat_id):
                    if not user.waiting(chat_id):
                        if len(db.column('waiting', 'id')) != 0:
                            user.make_session(chat_id)
                        else:
                            user.add_to_waiting(chat_id)
                            msg = "[رسالة من البوت 🤖]\n\nلقد تم اضافتك الى قائمة الانتظار، عندما يتم ايجاد شخص سوف يتم ارسال رسالة لك\nللالغاء ارسل /cancel"
                            bot.reply_to(message, msg)
                    else:
                        bot.reply_to(message, "[رسالة من البوت 🤖]\n\nانت في قائمة الانتظار حقا\nللالغاء ارسل /cancel")
                else:
                    bot.reply_to(message, "[رسالة من البوت 🤖]\n\nانت في جلسة حقا")
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
                msg = "[رسالة من البوت 🤖]\n\nاسمك الحالي هو: %s\n\nتنويه:\nهذا الاسم سوف يتم عرضه لاي شخص تحادثه عبر البوت" % username
            else:
                msg = "[رسالة من البوت 🤖]\n\nلم يتم انشاء اسم لك بعد.\nلانشاء اسم ارسل /new_name"
            bot.reply_to(message, msg)
        elif text.startswith("/cancel"):
            if user.waiting(chat_id):
                user.del_waiting(chat_id)
                bot.reply_to(message, "[رسالة من البوت 🤖]\n\nلقد تم الغاء البحث عن جلسة بنجاح")
            else:
                bot.reply_to(message, "[رسالة من البوت 🤖]\n\nانت لست بجلسة للبحث عن جلسة ارسل /search")
        elif text.startswith("/kill"):
            if user.in_sessions(chat_id):
                sessions_id = db.row('chat_sessions', 'user_id', chat_id, 'sessions')
                user.delete_sessions(sessions_id, chat_id)
                msg = "[رسالة من البوت 🤖]\n\nلقد تم قطع الجلسة بنجاح\nللبحث عن جلسة اخرى /search"
                bot.reply_to(message, msg)
            else:
                msg = "[رسالة من البوت 🤖]\n\nانت لست في جلسة حقا"
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
                                                            "video", "video_note", "voice", "animation"])
def message_handler(message):
    chat_id = str(message.chat.id)
    msg_id = str(message.id)
    # اذا كان هناك جلسة
    if user.in_sessions(chat_id):
        partner_id =  user.partner(chat_id)
        # التحقق ان وقت الجلسة لم ينتهي
        if time.time() < float(user.sessions_time(chat_id)):
            reply_msg_id = str(message.reply_to_message.id) if message.reply_to_message else None
            if message.text == "مسح":
                if reply_msg_id:
                    # اخذ ايدي الرسلة عند شريك الجلسة لحذفها
                    partner_msg_id = user.partner_msg_id(chat_id, reply_msg_id)
                    # اذا كانت الرسالة من المرسل، وفي الجلسة
                    if bool(list(filter(lambda m_id: m_id == reply_msg_id, 
                                            db.row("sessions_messages", "user_id", chat_id, "msg_id")))):
                        for message_be_delete in [(partner_id, partner_msg_id),
                                                    (chat_id, msg_id),
                                                        (chat_id, reply_msg_id)]:
                            c_id, m_id = message_be_delete
                            bot.delete_message(c_id, m_id)
                    else:
                        bot.reply_to(message, "[رسالة من البوت 🤖]\n\nالرسالة ليست موجودة في الجلسة او انها ليست لك")
                else:
                    bot.reply_to(message, "[رسالة من البوت 🤖]\n\nيجب عمل ربلي على الرسالة التي تريد مسحها من عند الطرف الثاني")
            else:
                # اذا تم الرد على رسالة
                if reply_msg_id:
                    sender.reply_message(message, chat_id, reply_msg_id)
                # اذا لم يتم الرد على رسالة
                else:
                    sender.send_to_partner(message, chat_id)
        else:
            # ايقاف الجلسة اذ انتها وقتها
            sessions_id = user.get_sessions(chat_id)
            user.kill_session(sessions_id)
            msg = "[رسالة من البوت 🤖]\n\nلقد انتهى وقت الجلسة، للبحث عن جلسة اخرى /search"
            for u_id in [chat_id, partner_id]:
                    bot.send_message(u_id, msg)            
    # اذ لم يكن في جلسة، سوف يتم تجاهل الرسالة
    else:
        pass

@bot.edited_message_handler(func=lambda msg:True, content_types= ["text", "document", "photo",
                                                            "video", "voice", "animation"])
def edit_message_handler(message):
    chat_id = str(message.chat.id)
    msg_id = str(message.id)
    if user.found(chat_id):
        if user.in_sessions(chat_id):
            sender.edit_message(msg_id, chat_id, message)
        else:
            pass
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
            bot.send_message(user_id, "[رسالة من البوت 🤖]\n\nلتحديث الاسم المستعار ارسل /new_name")
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