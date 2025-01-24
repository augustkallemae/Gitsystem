from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Define your bot token
TOKEN = "7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw"

async def start(update: Update, context):
    chat_id = update.effective_chat.id
    print(f"Chat ID: {chat_id}")
    await context.bot.send_message(chat_id=chat_id, text=f"Your chat ID is: {chat_id}")

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add a command handler
app.add_handler(CommandHandler("start", start))

# Run the bot
app.run_polling()
