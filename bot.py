
import json
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
from quotes import quotes, tips

TOKEN = "YOUR_BOT_TOKEN"
USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(list(users), f)

user_ids = load_users()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_ids.add(update.message.chat_id)
    save_users(user_ids)
    await update.message.reply_text(
        "Сәлем! Бұл — Сенім бөлмесі 🤗\nМаған өз ойыңды жаза аласың, мен саған мотивация мен қолдау беремін.\n"
        "/tip командасын қолданып пайдалы кеңес ала аласың."
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📌 Кеңес: {random.choice(tips)}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_ids.add(update.message.chat_id)
    save_users(user_ids)
    response = f"Сені түсінемін. Сен жалғыз емессің 💛\n\nЦитата: \"{random.choice(quotes)}\""
    await update.message.reply_text(response)

async def send_daily_quotes(application):
    for user_id in user_ids:
        try:
            await application.bot.send_message(chat_id=user_id, text=f"🌞 Күннің мотивациясы:\n\"{random.choice(quotes)}\"")
        except Exception as e:
            print(f"Қате: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tip", tip))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    scheduler = BackgroundScheduler()
    scheduler.add_job(send_daily_quotes, trigger='cron', hour=9, minute=0, args=[app])
    scheduler.start()

    print("✅ Бот іске қосылды...")
    app.run_polling()
