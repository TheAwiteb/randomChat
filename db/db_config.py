import sqlite3
import threading

coon = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = coon.cursor()
lock = threading.Lock()

# يتم وضع اسماء الجداول مع الاعمدة الخاصة بها في هذا القاموس
tablesName = {
        'users':['id', 'username'],
        
            }