import db
from .del_session_message import del_session_message

def kill_session(session_id:str):
    """ اغلاق الجلسة

    Args:
        session_id (str): ايدي الجلسة
    """
    del_session_message(session_id)
    db.del_row('sessions_messages', 'session', session_id)
    db.del_row('chat_sessions', 'sessions', session_id)