from .markup_config import MARKUP, BUTTON

def make_username():
    markup = MARKUP()
    markup.add(
        BUTTON(text="اضغط هنا لادخال الاسم", callback_data="username")
    )
    return markup