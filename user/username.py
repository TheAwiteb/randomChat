import db

def username(user_id:str):
    """ استخراج اسم الشخص من قاعدة البيانات

    Args:
        user_id (str): الايدي الخاص بالشخص

    Returns:
        [str]: الاسم الخاص بالشخص
    """
    return db.row('users', 'id', user_id, 'username')