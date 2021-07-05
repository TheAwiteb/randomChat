"""
انشاء قاعدة بيانات
"""
from db import make, insert

if __name__ == '__main__':
    make()
    insert(table_name='message', args=("start", "اهلا مع هذا البوت تستطيع المحادثة بسرية تامة مع شخص عشوائي ومجهول الهوية\nيمكنك الاطلاع على السورس كود من [هنا](https://github.com/Awiteb/randomChat)"))
    insert(table_name='message', args=("help", "اهلا طريقة استخدام البوت بسيطة جدا\nيمكنك بدا جلسة عبر هذا الامر /search\nويمكنك تغير الاسم المستعار الخاص بك عبر هذا الامر /new_name\nويمكنك قطع الجلسة التي بينك وبين العضو الاخر عبر هذا الامر /kill"))
    insert(table_name='message', args=("no_user", "اهلا بك، قبل البدء في دخول الجلسات يجب عليك اختيار اسم مستعار لك  \n \n تنويه: \n سوف يتم عرض الاسم المستعار للشخص المشارك معك بالجلسة"))
    insert(table_name='message', args=("not_private", "عذرا لحفظ خصوصية المستخدمين لايمكن انشاء جلسة في محادثة عامة"))