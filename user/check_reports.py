import db
from config import bot, max_reports

def check_reports(message, user_id):
    
    user_reports = db.row('users', "id", user_id, "reports")
    if user_reports:
        if int(user_reports) < max_reports:
            return True
        else:
            bot.reply_to(message, "لقد ,وصلت الي حد البلاغات وهو %s، عدد البلاغات التي لديك %s\n\nيحافظ حد البلاغات على استقرار البوت" % (max_reports, user_reports))
            return False
    else:
        return True