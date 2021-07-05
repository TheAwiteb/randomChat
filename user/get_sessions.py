import db

def get_sessions(user_id:str):
    """ ارجاع ايدي الجلسة التي يوجد بها المستخدم

    المتغيرات:
        user_id (str): الخص الذي تريد كعرفة ايدي الجلسة الخاصة به

    المخرجات:
        [str,None]: ايدي الجلسة ولاشي اذ لم تكن موجودة
    """
    return db.row("chat_sessions", 'user_id', user_id, 'sessions')