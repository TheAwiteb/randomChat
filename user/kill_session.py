import db

def kill_session(session_id:str):
    """ اغلاق الجلسة

    Args:
        session_id (str): ايدي الجلسة
    """
    db.del_row('chat_sessions', 'sessions', session_id)