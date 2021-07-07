from .db_config import (cursor, lock)

def row(table_name:str, column:str, word:str, want='*', lst=True):
    """ جلب صف من قاعدة البيانات

    المتغيرات:
        table_name (str): اسم الجدول الذي يوجد به العمود
        column (str): اسم العمود اذي يوجد به الصف
        word (str): القيمة الموجود في العمود
        want (str, optional): word العمود الذي تريده من الصف الذي يوجد به العمود الي قيمته. Defaults to '*'.
        lst (bool, optional): اخراج المعطيات كلستة ام تيبل. Defaults to 'True'.

    المخرجات:
        [list,tuple,str,None]: قائمة بالنتائج او عنصر او لاشي اذ لم تكن هناك نتائج
    """
    try:
        lock.acquire(True)
        cursor.execute(f"SELECT {want} FROM {table_name} WHERE {column}='{word}'")
        if lst:
            result = list(map(
                        lambda val: str(val).replace('<br>', '\n'),
                            [val for t in cursor.fetchall() for val in t]
                            ))
        else:
            result = list(map(
                        lambda t: tuple(str(val) for val in t),
                            [t for t in cursor.fetchall()]
            ))
        if lst:
            if (len(result) == 0):
                return None
            elif (len(result) == 1):
                return result[0] if lst else result[0][0]
            else:
                pass # سوف يتم تنفيد اخخر سطر وارجاع النتائج كلها
        else:
            pass # سوف يتم تنفيد اخخر سطر وارجاع النتائج كلها
        return result
    finally:
        lock.release()