from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from quotes import quotes, tips
import random

# /start командасы
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Сәлем! Бұл бот саған анонимді қолдау көрсетеді.\n"
        "Өзіңнің ойыңды жаза бер — мен сені қолдаймын.\n"
        "Егер кеңес керек болса, /tips командасын бас."
    )

# /tips командасы → пайдалы кеңес жібереді
async def send_tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(tips))

# Кез келген хабарлама келгенде → мотивация жібереді
async def respond_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(quotes))

# Ботты іске қосу
app = ApplicationBuilder().token("7564426395:AAHVOsUQjG1VoMdhL8Y72Kn7iftzD0DHX74").build()

# Командалар мен хабарламалар
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tips", send_tip))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_to_message))

# Ботты қосу
app.run_polling()
