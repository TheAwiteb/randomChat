import db
from config import  bot, session_time
from .username import username
from .del_waiting import del_waiting
from random import choice
from time import time

def make_session(user_id):
    """ انشاء جلسة بين اثنين

    المتغيرات:
        user_id (str): الايدي الخاص بالشخص المراد بحث جلسة له
    """
    # اذا تم العثور على منتظرين
    if len(db.column('waiting', 'id')) > 0:
        user_id2 = choice(db.column('waiting', 'id'))
        session_id = user_id+user_id2
        del_waiting(user_id2)
        for user in [user_id, user_id2]:
            db.insert('chat_sessions', (session_id, user, time()+session_time))
            bot.send_message(user, "تم انشاء جلسة مع %s\n\لقطع الجلسة ارسل /kill" % username(user_id if user_id != user else user_id2))
    # الغاء انشاء جلسة
    else:
        pass