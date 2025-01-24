from telegram import Bot
from telegram.ext import Application, CommandHandler

# Määrake oma token ja chat_id
TOKEN = "7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw"
chat_id = '6386153583'

# Defineeri käsklus, mis saadab sõnumi
async def start(update, context):
    await context.bot.send_message(chat_id=chat_id, text="Bot on aktiivne ja töötab!")

async def send_signal(update, context):
    await context.bot.send_message(chat_id=chat_id, text="SIIN ON SINU SIGNAAL!")

# Põhi funktsioon
def main():
    # Loome rakenduse objekti
    application = Application.builder().token(TOKEN).build()

    # Lisame käsu /start
    application.add_handler(CommandHandler("start", start))

    # Lisame käsu signaali saatmiseks
    application.add_handler(CommandHandler("signal", send_signal))

    # Alustame bot'i tööle panemist
    application.run_polling()

if __name__ == '__main__':
    main()
