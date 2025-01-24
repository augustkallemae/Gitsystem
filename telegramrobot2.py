import time
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Lase oma token ja chat ID siia
TOKEN = '7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw'  # Asenda oma tokeniga
CHAT_ID = '6386153583'  # Asenda oma chat ID-ga

def start(update, context):
    """Saatke sõnum kanalile, kui kasutaja käivitab käsu /start"""
    context.bot.send_message(chat_id=CHAT_ID, text="Tere! Olen sinu bot ja saadad signaale!")

def send_signal(update, context):
    """Saada signaal kasutajale"""
    context.bot.send_message(chat_id=CHAT_ID, text="XAUUSD SELL signaal\nENTRY: 2743.310\nSL: 2760.000\nTP: 2725.000")

def main():
    """Põhiprogramm, et käivitada bot ja alustada käskude töötlemist"""
    # Ühenda botiga
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Lisa käsud
    dp.add_handler(CommandHandler("start", start))  # Start käsk
    dp.add_handler(CommandHandler("signal", send_signal))  # Saada signaal käsu abil

    # Alusta bot'i töötamist
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
