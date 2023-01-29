from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from command_bot import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6142956852:AAGdjch5LLp_JStBRG-xJQBZ6hSJfLltuRg").build()

app.add_handler(CommandHandler("hi", hi_coomand))
app.add_handler(CommandHandler("time", time_coomand))
app.add_handler(CommandHandler("help", help_coomand))
app.add_handler(CommandHandler("sum", sum_coomand))
app.add_handler(CommandHandler("no_mat", no_mat_coomand))
app.add_handler(CommandHandler("joke", joke_coomand))
app.run_polling()