import db
from config import bot, max_reports
from telebot.types import Message

def make_report(message:Message, chat_id:str, username:str, partner_id:str):
    """ الابلاغ على شريك في الجلسة

    المتغيرات:
        message (Message): الرسالة التي محتواها رسالة الابلاغ
        chat_id (str): ايدي المبلغ
        username (str): اسم المبلغ
        partner_id (str): ايدي المبلغ عليه
    """
    users = db.row("users", "id", partner_id, "users_reports")
    user_reports = int(db.row('users', "id", partner_id, "reports"))
    bot.reply_to(message, "تم الابلاغ بنجاح")
    if chat_id in users.split():
        pass
    else:
        bot.send_message(partner_id, "تم الابلاغ عليك من قبل %s، عدد البلاغات الباقية حتى يتم حظرك %s" % (username, (max_reports) - (user_reports+1)))
        users += " %s" % chat_id
        db.update("users", "users_reports", users, "id", partner_id)
        db.update("users", "reports", user_reports+1, "id", partner_id)