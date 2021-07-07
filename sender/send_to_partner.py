from telebot.types import Message
from .get_reply import get_reply
from .send_message import send_message
import db
import user
import markup

def send_to_partner(message:Message, chat_id:str):
    """ ارسال الرسالة الى رفيق الشخص

    Args:
        message (telebot.types.Message): الرسالة
        chat_id (str): الشخص الذي يريد ارسالها
    """
    reply, replyType, text = get_reply(message)
    partner_id = user.partner(chat_id)
    session_id = user.get_sessions(chat_id)
    msg_id = message.id
    partner_msg_id = send_message(partner_id, replyType, reply, text,
                    markup.username(chat_id), msg_id=None)
    db.insert("sessions_messages", [session_id, chat_id, msg_id, partner_msg_id])