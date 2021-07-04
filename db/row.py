from .db_config import (cursor, lock)

def row(table_name:str, column:str, word:str, want='*'):
    """ جلب صف من قاعدة البيانات

    المتغيرات:
        table_name (str): اسم الجدول الذي يوجد به العمود
        column (str): اسم العمود اذي يوجد به الصف
        word (str): القيمة الموجود في العمود
        want (str, optional): word العمود الذي تريده من الصف الذي يوجد به العمود الي قيمته. Defaults to '*'.

    المخرجات:
        [list,str,None]: قائمة بالنتائج او عنصر او لاشي اذ لم تكن هناك نتائج
    """
    try:
        lock.acquire(True)
        cursor.execute(f"SELECT {want} FROM {table_name} WHERE {column}='{word}'")
        result = list(map(
                    lambda val: str(val),
                        [val for table in cursor.fetchall() for val in table]
                        ))
        if (len(result) == 0):
            return None
        elif (len(result) == 1):
            return result[0]
        else:
            return result
    finally:
        lock.release()