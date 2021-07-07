from .get_session_messages import get_session_messages
from .partner import partner
from config import bot

def del_session_message(session_id:str):
    """ مسح الرسائل التي رسل في الجلسة

    Args:
        session_id (str): ايدي الجلسة
    """
    for message in get_session_messages(session_id):
        user_id = message[0]
        msg_id = message[1]
        partner_msg_id = message[2]
        partner_id = partner(user_id)
        try:
            bot.delete_message(user_id, msg_id)
            bot.delete_message(partner_id, partner_msg_id)
        except Exception:
            pass # عدم فعل شي عند ظهور خطأ عدم وجود الرسالة