import db

def del_waiting(user_id:str):
    """ مسح الشخص من قائمة المنتظرين

    Args:
        user_id (str): الشخص المراد مسحه
    """
    db.del_row('waiting', 'id', user_id)