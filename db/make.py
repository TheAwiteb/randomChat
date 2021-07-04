from config import TOKEN
from .db_config import (cursor, coon, 
                            tablesName)

def make():
    """
    دالة انشاء قاعدة البيانات
    """
    # التحقق من انه تم وضع التوكن الخاص بالبوت ام لا
    if TOKEN == "":
        raise Exception("config يجب عليك وضع التوكن الخاص بالبوت في ملف")
    else:
        # يتم انشاء قاعدة البيانات عبر اللوب التالية
        for table in tablesName:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS '{table}'(
                            {','.join(tablesName.get(table))}
                            )""")
            coon.commit()