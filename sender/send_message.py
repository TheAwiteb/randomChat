from config import bot

def send_message(chat_id, replyType, reply, text, markup=None, msg_id=None):
    """ ارسال رسالة الى مستخدم

    المتغيرات:
        chat_id (str): المستخدم المراد ارسال الرسالة له
        replyType (str): نوع الرسالة
        reply (str): النص، او ايدي الملف المراد ارساله
        text (str): نص الرسالة او ال شرح الملف
        markup (telebot.types.InlineKeyboardMarkup, optional): الازرار. Defaults to None.
        msg_id (str,int, optional): ايدي الرسالة لعمل ربلي لها. Defaults to None.
    المخرجات:
        [int]: ايدي الرسالة التي تم ارسالها
    """
    
    if replyType == "text":
        msg = bot.send_message(chat_id=chat_id, text=reply, reply_to_message_id=msg_id,
                            reply_markup=markup, )
    elif replyType == "audio":
        msg = bot.send_audio(chat_id=chat_id, audio=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "document":
        msg = bot.send_document(chat_id=chat_id, data=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "photo":
        msg = bot.send_photo(chat_id=chat_id, photo=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "sticker":
        msg = bot.send_sticker(chat_id=chat_id, data=reply,
                            reply_to_message_id=msg_id, reply_markup=markup)
    elif replyType == "video":
        msg = bot.send_video(chat_id=chat_id, data=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "video_note":
        msg = bot.send_video_note(chat_id=chat_id, data=reply,
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "voice":
        msg = bot.send_voice(chat_id=chat_id, voice=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "animation":
        msg = bot.send_animation(chat_id=chat_id, animation=reply, caption=text, reply_to_message_id=msg_id,
                            reply_markup=markup)
    else:
        return
    return msg.id