
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Расширенный список мотивационных цитат
quotes = [
    "Сен мықтысың! Ешқашан берілме!",
    "Бәрі жақсы болады, тек сеніміңді жоғалтпа.",
    "Қателік – жетістікке апарар жол!",
    "Сен жалғыз емессің. Біз бірге бәрін еңсереміз.",
    "Кішкентай қадам – үлкен жетістікке бастар жол.",
    "Сенің арманың – сенің күшің.",
    "Бүгінгі күш – ертеңгі табыстың кілті.",
    "Әр күн – жаңа мүмкіндік.",
    "Өзіңе сен, сонда бәрі мүмкін.",
    "Сен – өз өміріңнің авторы!",
    "Сенің ойың маңызды. Бөлісуден қорықпа.",
    "Сенің құның сенің бағаңмен өлшенбейді.",
    "Бүгін қиын болса да, ертең жарқын болады.",
    "Ұмытпа: сен ерекше және қайталанбассың!",
    "Бір сәт тынығып ал — бұл да алға жылжу.",
    "Жай ғана тыныс ал. Сен бәрін істей аласың.",
    "Ешкім мінсіз емес, бірақ әркімнің құндылығы бар.",
    "Сәтсіздік – тек тәжірибе. Жолыңды жалғастыр.",
    "Мейірімділік пен түсіністік – үлкен күш.",
    "Сенің болашағың – жарқын және шексіз."
]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Сәлем! Бұл бот анонимді түрде саған қолдау көрсетеді. Жай ғана /tips командасын басып, мотивациялық ой ал!"
    )

# Команда /tips
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(quotes))

# Запуск приложения
app = ApplicationBuilder().token("7564426395:AAHVOsUQjG1VoMdhL8Y72Kn7iftzD0DHX74").build()

# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tips", tips))

# Запуск бота
app.run_polling()
