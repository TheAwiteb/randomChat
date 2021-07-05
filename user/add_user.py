from config import bot
from .save_username import save_username

def add_user(user_id:str, new_user:bool):
    """ الدخول الى دالة تغير الاسم

    المتغيرات:
        user_id (str): الايدي الخاص بالشخص
        new_user (bool): هل تود اضافته كمستخدم جديد ام تغير اسم المستخدم فقط
    """
    msg = bot.send_message(user_id, "للالغاء ارسل: /cancel\n ارسل الاسم المستعار الان")
    bot.register_next_step_handler(msg, save_username, user_id, new_user)