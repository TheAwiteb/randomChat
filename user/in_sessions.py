import db

def in_sessions(user_id:str):
    """ التحقق هل الشخص موجود في جلسة ان لا

    المتغيرات:
        user_id (str): ايدي الشخص

    المحرجات:
        [bool]: موجود ام لا
    """
    # false اذا كانت اللستة فاضية سوف يرجع
    return bool(list(
        filter(
            lambda u_id: u_id == user_id,
                db.column('chat_sessions', 'user_id')
        )
    ))