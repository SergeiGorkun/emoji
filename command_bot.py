from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import requests

async def hi_coomand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'hi {update.effective_user.first_name}')

async def help_coomand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/joke ')

async def time_coomand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def joke_coomand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
    json = response.json()
    joke = json['joke']
    await update.message.reply_text(joke)

async def sum_coomand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    res = f'{x} + {y} = {x+y}'

    if update.effective_user.first_name == 'Дмитрий':
        res = 'Офигел? Пошел в анус'
    await update.message.reply_text(res)

async def no_mat_coomand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f' {update.effective_user.first_name} Никогда не ругайся матом! Всё будет хорошо!')