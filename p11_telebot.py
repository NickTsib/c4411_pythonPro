# 8066585778:AAEsH2JbJgvIk1SD0T8w10jHWssdUKPVMvw
import datetime
from random import randint, choice
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8066585778:AAEsH2JbJgvIk1SD0T8w10jHWssdUKPVMvw"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}")

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    dice_result = randint(1, 6)
    await update.message.reply_text(f"Your dice: {dice_result}")

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    res = choice(["rock", "scissors", "paper"])
    await update.message.reply_text(f"My item: {res}")

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now_date = datetime.date.today()
    ny_date = datetime.date(datetime.date.today().year + 1, 1, 1)
    result = ny_date - now_date
    await update.message.reply_text(f"Days until NY: {result}")

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}\nYou said: {text}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("roll", dice))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("newy", new))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))
app.run_polling()
