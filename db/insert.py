from .db_config import (cursor, coon, 
                        tablesName, lock)

def insert(table_name:str, args:tuple):
    """ ادخال البيانات داخل قاعدة البيانات
    المتغيرات:
        table_name (str): اسم الجدول المراد ادخال البيانات فيه
        args_ (tuple): القيم التي سوف تملي بها الاعمدة الخاصة بالجدول
    """
    try:
        lock.acquire(True)
        args = tuple(map(
                lambda ar:str(ar).replace('\n', '<br>'), 
                args
                ))
        first_element = f"('{args[0]}')"
        cursor.execute(f"INSERT INTO {table_name} ({','.join(tablesName[table_name])}) VALUES {tuple(args) if len(args) > 1 else first_element}")
        coon.commit()
    finally:
        lock.release()