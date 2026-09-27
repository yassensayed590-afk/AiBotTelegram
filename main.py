import telebot

# ضع هنا الTOKالسري الذي أخذته من BotFather بين العلامتين ""
TOKEN = "8902072720:AAEZH8YNFfE3OI5nfbLt2uoRULvFJDiMzyw"

bot = telebot.TeleBot(TOKEN)

# عندما يضغط المستخدم على Start
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت الذكاء الاصطناعي الشامل. اكتب لي أي شيء لأرد عليك، أو اكتب (ارسم ...) لأصنع لك صورة أنمي!")

# إذا طلب المستخدم رسم صورة
@bot.message_handler(func=lambda msg: msg.text.startswith("ارسم"))
def draw_anime(message):
    prompt = message.text.replace("ارسم", "").strip()
    bot.reply_to(message, "جاري تصميم صورتك الأنمي بالذكاء الاصطناعي... 🎨")
    
    # محرك مجاني وسريع لتوليد الصور فوراً
    img_url = f"https://pollinations.ai{prompt}?width=1024&height=1024&nologo=true"
    bot.send_photo(message.chat.id, img_url, caption="إليك التصميم الخاص بك!")

# للرد الذكي العادي على أي كلام
@bot.message_handler(func=lambda msg: True)
def chat(message):
    bot.reply_to(message, f"أنت تقول: '{message.text}'. أنا بوت ذكي وجاري ربط محرك الألعاب الكامل الخاص بي لتنفيذ طلباتك الكبيرة!")

# تشغيل البوت بدون توقف
bot.infinity_polling()
