from .db_config import (coon, cursor, 
                            lock)

def del_row(table_name:str, column:str, value:str):
    """ حذف صف من قاعدة البيانات
    المتغيرات:
        table_name (str): اسم الجدول الذي يوجد به العامود
        column (str): اسم العامود الذي يوجد به الصف
        value (str): القيمة التي تريد مسحها الموجودة في العامود
    """
    value = value.replace('\n', '<br>')
    try:
        lock.acquire(True)
        cursor.execute(f"DELETE FROM {table_name} WHERE {column}='{value}'")
        coon.commit()
    finally:
        lock.release()