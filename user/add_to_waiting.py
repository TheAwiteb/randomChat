import db
from .make_session import make_session

def add_to_waiting(user_id:str):
    """ اضافة الشخص الى قائمة الانتظار

    المتغيرات:
        user_id (str): الايدي الخاص بالمستخدم
    """
    # اذا كانت قائمة الانتظار ليست فاضية انشئ جلسة
    if len(db.column('waiting', 'id')) > 0:
        make_session(user_id)
    else:
        # اضافة العضو الى قائمة الانتظار
        db.insert('waiting', (user_id,))