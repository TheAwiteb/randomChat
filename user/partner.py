import db
from .get_sessions import get_sessions

def partner(user_id:str):
    """ جلب شريك الجلسة الخاصة ب المستخدم

    المتغيرات:
        user_id (str): ايدي المستخدم الذي تريد شريكه

    المخرجات:
        [str,None]: ايدي الشريك او لاشي
    """
    session_id = get_sessions(user_id)
    partner_id = ''.join(list(filter(
            lambda u_id: u_id!=user_id,
                db.row('chat_sessions', 'sessions', session_id, 'user_id')
    )))
    return partner_id