import logging
from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask, request
import asyncio

# Teie bot token
TOKEN = '7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw'
# Teie kanalite chat ID
CHAT_ID = '6386153583'

app = Flask(__name__)

# Looge bot logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Kõigepealt defineerige käsk funktsioon, mis saadab sõnumi kanalile
def start(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="Tere, bot töötab!")

# Loo Application
application = ApplicationBuilder().token(TOKEN).build()

# Lisage käskude käitleja
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Defineeri webhooki käsitleja
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    if request.method == 'POST':
        json_str = request.get_data().decode('UTF-8')
        update = application.bot.get_updates()
        for upd in update:
            application.process_update(upd)
        return 'OK'

# Loo käsk, mis saadab sõnumi Telegrami kanalile
async def send_message_to_channel():
    await application.bot.send_message(chat_id=CHAT_ID, text="Test sõnum kanalile.")
    print("Sõnum saadetud! ")

# Kõik vajalikud hookid ja konfigureerimine
if __name__ == '__main__':
    asyncio.run(application.bot.set_webhook(f'https://abcd1234.ngrok.io/{TOKEN}'))
    asyncio.run(send_message_to_channel())  # Saada testisõnum kanalisse
    app.run(host='0.0.0.0', port=5000, debug=True)
