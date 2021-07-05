"""
عبر هذا الملف يتم ملئ المعلومات الاساسية
https://t.me/BotFather يمكنك جلب التوكن الخاص بالبوت عبر هذا البوت
"""

VERSION = "v1.2.0"

# ضع توكن البوت هنا
TOKEN = str("")

# اختار اقصى مدة للجلسة
session_time = 60*20 # 20m in seconds

# لسهولة استعمال المتغيرات بين الملفات
import telebot
bot = telebot.TeleBot(TOKEN)
botName = bot.get_me().first_name