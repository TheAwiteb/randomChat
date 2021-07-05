from config import bot

def send_message(chat_id, replyType, reply, text, markup=None, msg_id=None):
    """ ارسال رسالة الى مستخدم

    Args:
        chat_id (str): المستخدم المراد ارسال الرسالة له
        replyType (str): نوع الرسالة
        reply (str): النص، او ايدي الملف المراد ارساله
        text (str): نص الرسالة او ال شرح الملف
        markup (telebot.types.InlineKeyboardMarkup, optional): الازرار. Defaults to None.
        msg_id (str,int, optional): ايدي الرسالة لعمل ربلي لها. Defaults to None.
    """
    if replyType == "text":
        bot.send_message(chat_id=chat_id, text=reply, reply_to_message_id=msg_id,
                            reply_markup=markup, )
    elif replyType == "audio":
        bot.send_audio(chat_id=chat_id, audio=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "document":
        bot.send_document(chat_id=chat_id, data=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "photo":
        bot.send_photo(chat_id=chat_id, photo=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "sticker":
        bot.send_sticker(chat_id=chat_id, data=reply,
                            reply_to_message_id=msg_id, reply_markup=markup)
    elif replyType == "video":
        bot.send_video(chat_id=chat_id, data=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "video_note":
        bot.send_video_note(chat_id=chat_id, data=reply,
                        reply_to_message_id=msg_id, reply_markup=markup, )
    elif replyType == "voice":
        bot.send_voice(chat_id=chat_id, voice=reply, caption=text if text != 'None' else "",
                        reply_to_message_id=msg_id, reply_markup=markup, )
    else:
        pass