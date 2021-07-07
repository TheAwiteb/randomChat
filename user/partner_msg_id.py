import db

def partner_msg_id(chat_id:str, msg_id:str):
    """ جلب ايدي الرسالة المدخل ايديها عند شريكك في المحادثة

    المتغيرات:
        chat_id (str): ايدي المرسل
        msg_id (str): ايدي الرسالة المراد معرفة ايديها عند الشريك

    المخرجات:
        [str]: ايدي الرسالة
    """
    msg_id = list(filter(
                lambda t: t[0] == msg_id,
                    db.row("sessions_messages", "user_id", chat_id, 'msg_id,msg_id_in_partner', lst=False)
    )) # اخذ العنصر الثاني من العنصر الاول
    return msg_id[0][1] if msg_id else None