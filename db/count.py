from .db_config import (cursor, lock)

def count(table_name:str, column:str, word:str):
    """ يجلب لك مرات تكرار ال القيمة في ال العمود
    المتغيرات:
        table_name (str): اسم الجدول الذي يوجد به العمود.
        column (str): العمود الذي يوجد فيه القيمة التي تريد معرفة عدد تكرارها.
        word (str): القيمة التي تريد معرفة عدد تكرارها.
    المخرجات:
        int: عدد تكرار القيمة في العمود.
    """
    try:
        lock.acquire(True)
        cursor.execute(f"SELECT COUNT() FROM {table_name} WHERE {column}='{word}'")
        return cursor.fetchone()[0]
    finally:
        lock.release()