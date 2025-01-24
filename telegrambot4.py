import logging
from telegram import Bot
from telegram.ext import CommandHandler, Dispatcher, Updater
from flask import Flask, request

# Teie bot token
TOKEN = '7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw'
# Teie kanalite chat ID
CHAT_ID = '6386153583'

app = Flask(__name__)

# Määrake bot ja registreerige webhook
bot = Bot(TOKEN)
updater = Updater(bot=bot)
dispatcher = updater.dispatcher

# Looge bot logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Kõigepealt defineerige käsk funktsioon, mis saadab sõnumi kanalile
def start(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="Tere, bot töötab!")

# Defineeri webhooki käsitleja
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    if request.method == 'POST':
        json_str = request.get_data().decode('UTF-8')
        update = updater.bot.get_updates()
        dispatcher.process_update(update)
        return 'OK'

# Loo käsk, mis saadab sõnumi Telegrami kanalile
def send_message_to_channel():
    bot.send_message(chat_id=CHAT_ID, text="Test sõnum kanalile.")
    print("Sõnum saadetud! ")

# Lisage käsud
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Määrake webhook URL
@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def handle_webhook():
    if request.method == 'POST':
        json_str = request.get_data().decode('UTF-8')
        update = updater.bot.get_updates()
        dispatcher.process_update(update)
    return 'ok'

# Kõik vajalikud hookid ja konfigureerimine
if __name__ == '__main__':
    bot.set_webhook(f'https://YOUR_SERVER_URL/{TOKEN}')
    app.run(host='0.0.0.0', port=5000, debug=True)

