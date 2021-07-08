<h1 align="center">
  <br>
  <a><img width="450" height="400" src="./img/randomChatBBOT_image.jpg" alt="randomChat - img"></a>
  <br>
  randomChat
  <br>
</h1>


<p align="center">بوت المحادثات العشوائية، هو بوت يقوم بأنشاء جلسة بينك وبين عضو عشوائي اخر بسرية تامة</p>



<p align="center">
  <a href="#التنزيل">التنزيل</a>
  •
  <a href="#المميزات">المميزات</a>
  •
  <a href="#الاستعمال">الاستعمال</a>
  •
  <a href="#البوت">بوت لتجربة السورس</a>
  •
  <a href="#الرخصة">الرخصة</a>
</p>


<div dir="rtl">

## التنزيل

يتم استعمال [GitHub](https://github.com) لتنزيل مشروع البوت

<div dir="ltr">

```bash
# نسخ المشروع من جت هب
git clone https://github.com/Awiteb/randomChat

# تغير المسار الى مسار المشروع
cd randomChat

# تنزيل المكتبات المطلوبة لتشغيل البوت
pip3 install -r requirements.txt
```
<div dir="rtl">

>  تنويه: يجب ملئ ملف ال config
<div dir="ltr">

```bash
# انشاء قاعدة البيانات
python3 make_db.py

# تشغيل البوت
python3 main.py
```
<div dir="rtl">

## المميزات

* محادثة سرية مع افراد عشوائيين
* عدم تخزين شي في قاعدة البيانات، سوا الايدي الخاص بك في التلقرام
* مسح جميع الرسائل التي في الجلسة عند انتهائها تلقائياً
* القدرة على مسح وحذف وتعديل الرسالة في الجلسة

## الاستعمال

> تنويه: يتم ارسال هاذي الاوامر الى البوت في التلقرام

* <b>البحث عن جلسة عشوائية</b>

<div dir="ltr">

      /search
<div dir="rtl">

* <b>تغير اسم المستخدم، او انشاء</b>

<div dir="ltr">

      /new_name
<div dir="rtl">

* <b>اظهار اسمك المستعار</b>

<div dir="ltr">

      /my_name
<div dir="rtl">

* <b>قطع الجلسة</b>

<div dir="ltr">

      /kill

<div dir="rtl">

## البوت

[@randomChatBBot](https://t.me/randomChatBBot)

## الرخصة
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)