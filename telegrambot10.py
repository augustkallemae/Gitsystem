import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Lülita logimine sisse
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegrami boti token
TOKEN = '7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw'

# Kood, mis saadab sõnumi
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Tere, mina olen bot!')

# Asünkroonne funktsioon, mis töötab botiga
async def send_message_to_channel() -> None:
    application = Application.builder().token(TOKEN).build()

    # Käivita kommandihandler
    application.add_handler(CommandHandler('start', start))

    # Testige sõnumi saatmist kanalisse
    chat_id = "@fx_trading_vision_public"  # Sisestage oma kanalite ID
    await application.bot.send_message(chat_id=chat_id, text="Test sõnum kanalile.")

    # Käivitage bot
    await application.run_polling()

if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(send_message_to_channel())
    except Exception as e:
        logger.error(f"Bot'i käivitamine ebaõnnestus: {e}")
