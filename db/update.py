from .db_config import (coon, cursor, lock)

def update(table_name:str, column:str, new_value:str, where_column:str, where_value:str) -> None:
    new_value = str(new_value).replace('\n', '<br>')
    """update column in database
    المتغيرات:
        table_name (str): اسم الجدول.
        column (str): العمود الذي تريد تحديثه.
        new_value (str): القيمة الجديدة.
        where_column (str): where_value العمود الذي يوجد به.
        where_value (str): where_column القيمة الموجودة في.
    """
    where_value = where_value.replace('\n', '<br>')
    new_value = new_value.replace('\n', '<br>')
    try:
        lock.acquire(True)
        cursor.execute(f"UPDATE {table_name} SET '{column}'= '{new_value}' WHERE {where_column} = '{where_value}'")
        coon.commit()
    finally:
        lock.release()
