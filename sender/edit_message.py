import markup
from telebot import types
from .get_reply import get_reply
from config import bot
import user
import markup

def edit_message(meg_id:str, chat_id:str, new_message:types.Message):
    
    partner_id = user.partner(chat_id)
    partner_msg_id = user.partner_msg_id(chat_id, meg_id)
    reply, replyType, text = get_reply(new_message)
    edit(replyType, reply, text,
            partner_id, partner_msg_id, markup.username(chat_id))

def edit(replyType, reply, text,
            chat_id, msg_id, m):
    
    if replyType in ["text"]:
        if replyType == "voice":
            bot.edit_message_caption(text, chat_id, msg_id, reply_markup=m)
        else:
            bot.edit_message_text(reply, chat_id, msg_id, 
                                reply_markup=m)
    else:
        if replyType == "document":
            reply = types.InputMediaDocument(reply)
            
        elif replyType == "photo":
            reply = types.InputMediaPhoto(reply)
        elif replyType == "video":
            reply = types.InputMediaVideo(reply)
        elif replyType == "animation":
            reply = types.InputMediaAnimation(reply)
        elif replyType == "voice":
            reply = None
        else:
            return
        # انشاء التعديل بعد اخذ الميديا
        try:
            bot.edit_message_media(reply, chat_id, msg_id,reply_markup=m)
        except: # تحصل مشكلة عندما يتم تعديل شرح الملف بدون الملف
            pass # سوف يتم تجالها
        bot.edit_message_caption(text, chat_id, msg_id, reply_markup=m)