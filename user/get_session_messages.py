import db

def get_session_messages(session_id:str):
    """ حلب جيمع الرسائل التابعة للجلسة 

    المتغيرات:
        session_id (str): ايدي الجلسة المراد استخخراج معلوماتها
    
    المخرجات:
        list: الرسالة من عند المرسل والمستقبل مع ايدي المرسل
    """
    return (db.row("sessions_messages", "session", session_id, 'user_id, msg_id, msg_id_in_partner', lst=False))