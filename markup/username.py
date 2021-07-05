import user
from .markup_config import MARKUP, BUTTON

def username(user_id:str):
    """ عمل زر باسم الشخص

    المتغيرات:
        user_id (str): ايدي الشخص

    المخرجات:
        [telebot.types.InlineKeyboardMarkup]: الزر
    """
    markup = MARKUP()
    username = user.username(user_id)
    markup.add(BUTTON(text=username, callback_data=username)) # لايوجد قيمة مرجعة
    return markup