import db

def found(user_id:str):
    """ ارجاع اذا الايدي موجود في قاعدة البيانات ام لا

    المتغيرات:
        user_id (str): ايدي المستخدم

    المخرجات:
        bool: المستخدم موجود ام لا
    """
    # false اذا كانت اللستة فاضية سوف يرجع 
    return bool(list(
        filter(
            lambda u_id:u_id == user_id,
                db.column("users", "id")
                )
        ))
