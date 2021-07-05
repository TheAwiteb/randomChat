import db

def waiting(user_id:str):
    """ ارجاع اذا كان الشخص موجود في قائمة المنتظرين ام لا

    المتغيرات:
        user_id (str): الشخص المراد معرفة اذا كان موجود ام لا

    المخرجات:
        [bool]: موجود ام لا
    """
    return bool(list(filter(
            lambda u_id: u_id == user_id,
                db.column('waiting', 'id')
    )))