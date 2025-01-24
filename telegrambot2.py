import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging for debugging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Your bot's token from @BotFather
TOKEN = "7395583199:AAG4yw0Y-xwTP9U0UodCR-G6-D29CVUM32M"  # Replace with your bot token

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your trading bot. Ready to send signals!")

# Command to send a custom signal
async def send_signal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) < 3:
        await update.message.reply_text(
            "Usage: /send_signal <ENTRY> <STOP LOSS> <TAKE PROFIT>\nExample: /send_signal 1930.5 1910 1950"
        )
        return
    entry, sl, tp = context.args
    signal = f"🚨 *Trading Signal*\n\nEntry: {entry}\nStop Loss: {sl}\nTake Profit: {tp}"
    await update.message.reply_text(signal, parse_mode="Markdown")

# Main function to start the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send_signal", send_signal))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
