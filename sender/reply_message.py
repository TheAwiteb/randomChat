from telebot.types import Message
import db
import user
from .send_to_partner import send_to_partner

def reply_message(message:Message, user_id:str, reply_to:str):
    """ عمل ربلي لرسالة

    Args:
        message (Message): الرسالة المراد ارسالها مع ربلي لرسالة اخرى
        user_id (str): ايدي مرسل الرسالة
        reply_to (str): ايدي الرسالة المراد عمل ربلي لها
    """
    session_id = user.get_sessions(user_id)
    # اذا كانت الرسالة في الجلسة
    if list(filter(lambda t: reply_to in t,
                        db.row("sessions_messages", "session", session_id, "msg_id, msg_id_in_partner", lst=False))):
        # اخذ ايدي الشريك في الجلسة
        partner_id = user.partner(user_id)
        # اذا كانت الرسالة المعمول لها ربلي من المرسل
        if str(message.reply_to_message.from_user.id) == user_id:
            # اخذ ايدي الرسالة عند الشريك
            msg_id = [user.partner_msg_id(user_id, reply_to)]
        # اذ لم تكن الرسالة من المرسل
        else:
            msg_id = list(filter(
                    lambda t: t[1] == reply_to,
                        db.row("sessions_messages", "user_id", partner_id, "msg_id, msg_id_in_partner", lst=False)
            ))
    # اذا كانت الرسالة ليست في الجلسة
    else:
        # جعل قيمة الايدي لاشي لتجنب عمل ربلي
        msg_id = [None]
    msg_id = msg_id[0] if msg_id else None
    send_to_partner(message, user_id, msg_id)