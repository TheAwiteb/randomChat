import db

def sessions_time(user_id:str):
    """ ارجاع وقت انتهاء الجلسة التي يوجد بها المستخدم

    المتغيرات:
        user_id (str): الشخص المراد معرفة وقت انتهاء جلسته

    المخرجات:
        [float]: وقت الانتها
    """
    return db.row("chat_sessions", "user_id", user_id, "end_time")