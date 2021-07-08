import db
from telebot.types import Message
from config import bot
from time import time

def save_username(message:Message, user_id:str, new_user:bool):
    """ اضافة شخص الى قاعدة البيانات او تعديل اسمه

    المتغيرات:
        message (telebot.types.Message): كائن الرسالة
        user_id (str): الايدي الخاص بالمستخدم
        new_user (bool): اضافته الى قاعدة البيانات ام تغير اسمه فقط
    """
    username = message.text
    if username:
        # اذا كان الاسم امر
        if username.startswith('/'):
            if username == "/cancel":
                # الغاء العملية
                bot.reply_to(message, "تم الالغاء")
            else:
                msg = bot.reply_to(message, "للالغاء ارسل: /cancel\nالاسم المستعار يجب ان لا يبدا ب / \nحاول مجددا")
                bot.register_next_step_handler(msg, save_username, user_id, new_user)
        else:
            if len(username) <=10:
                # اذا المستخدم جديد يتم اضافته الى قاعدة البيانات
                if new_user:
                    db.insert('users', (user_id, username, time(), 0, ""))
                # اذا قديم يتم تحديث اسمه
                else:
                    db.update("users", 'username', username, 'id', user_id)
                bot.reply_to(message, "تم تحديث الاسم بنجاح الى '{}'".format(username))
            else:
                msg = bot.reply_to(message, "للالغاء ارسل: /cancel\nيجب ان لا يتخطى طول الاسم 10 خانات \nحاول مجددا")
                bot.register_next_step_handler(msg, save_username, user_id, new_user)
    else:
        msg = bot.reply_to(message, "للالغاء ارسل: /cancel\nالاسم المستعار يجب ان يكون نص\nحاول مجددا")
        bot.register_next_step_handler(msg, save_username, user_id, new_user)