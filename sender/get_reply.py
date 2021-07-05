from telebot.types import Message

def get_reply(message:Message):
    """ ارجاع الايدي و نوع ونص الرسالة

    Args:
        message (telebot.types.Message): الرسالة المراد استخراج البيانات منها

    Returns:
        : ارجاع الايدي و نوع ونص الرسالة
    """
    replyType = message.content_type
    text = message.text if replyType == 'text' else message.caption
    if replyType == "text":
        reply =  text
    elif replyType == "audio":
        reply =  message.audio.file_id
    elif replyType == "document":
        reply =  message.document.file_id
    elif replyType == "photo":
        reply =  message.photo[0].file_id
    elif replyType == "sticker":
        reply =  message.sticker.file_id
    elif replyType == "video":
        reply =  message.video.file_id
    elif replyType == "video_note":
        reply =  message.video_note.file_id
    elif replyType == "voice":
        reply =  message.voice.file_id
    else:
        return
    return reply, replyType, text