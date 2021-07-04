from .db_config import (cursor, lock)

def column(table_name:str, column:str):
    """ ترجع لك جميع القيم التي في العامود المعطى
    المتغيرات:
        table_name (str): اسم الجدول اذي يوجد فيه العامود
        column (str): اسم العامود الذي تريد اسخراج جميع القيم التي به
    المخرجات:
        list: قائمة من عناصر العامود
    """
    try:
        lock.acquire(True)
        cursor.execute(f"SELECT {column} FROM {table_name}")
        return list(map(
                lambda val: str(val).replace('<br>', '\n'),
                    [val for table in cursor.fetchall() for val in table]
                ))
    finally:
        lock.release()