import yfinance as yf
import pandas as pd
from datetime import datetime, timezone
from telegram import Bot
import time

# Telegram bot setup
bot_token = "7881974789:AAF0T1sv65Plfmk28mEiz2GdovGqbclAGbw"
channel_id = "@fx_trading_vision_public"
bot = Bot(token=bot_token)

# Function to check trading conditions
def check_trading_conditions():
    data = yf.download("XAUUSD=X", interval="5m", period="1d")
    data["SMA_20"] = data["Close"].rolling(window=20).mean()
    data["SMA_50"] = data["Close"].rolling(window=50).mean()
    
    if len(data) < 50:
        return None

    last_row = data.iloc[-1]
    previous_row = data.iloc[-2]

    if (
        previous_row["SMA_20"] <= previous_row["SMA_50"]
        and last_row["SMA_20"] > last_row["SMA_50"]
    ):
        entry_price = last_row["Close"]
        sl_price = entry_price * 0.99
        tp_price = entry_price * 1.02
        return entry_price, sl_price, tp_price

    return None

# Function to send a signal
def send_signal(entry, sl, tp):
    message = (
        f"🔔 Trading Signal 🔔\n\n"
        f"ENTRY: {entry:.2f}\n\n"
        f"SL: {sl:.2f}\n"
        f"TP: {tp:.2f}"
    )
    bot.send_message(chat_id=channel_id, text=message)

# Main function
def run_bot():
    print("Bot töötab! Kontrollin tingimusi...")
    while True:
        now = datetime.now(timezone.utc)  # Kasutab timezone-aware datetime'i
        if now.minute % 5 == 0:  # Kontrollib iga 5 minuti järel
            result = check_trading_conditions()
            if result:
                entry, sl, tp = result
                send_signal(entry, sl, tp)
                time.sleep(300)  # Väldib mitmekordseid signaale samal minutil
        time.sleep(1)

# Käivita bot
run_bot()

