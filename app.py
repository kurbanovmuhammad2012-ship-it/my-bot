import os
import threading
from flask import Flask
import telebot

# Токен берется из настроек Render (мы добавим его позже)
TOKEN = os.environ.get('9218629867:AAGyRcXJL5uH6zRnBCkhGQPI9o596ldtZtc')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Это тестовое задание. Напиши 'роналду', 'чебупель' или 'картошка'.")

# Твой обработчик
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if text == "роналду":
        bot.reply_to(message, "месси какашка ранальда барашка сууууу!")
    
    elif text == "чебупели":
        bot.reply_to(message, "бой чебупели чебупели чебупели бооооой чебупели это мой юз привет: @Siles_210")
    
    elif text == "картошка":
        bot.reply_to(message, "тут я ниче не придумал поэтосу картошка")
    
    else:
        bot.reply_to(message, f"ты че несешь я пока другие команды не знаю что это значит во '{message.text}'. нормально обдайся чушпан")

# --- ЧАСТЬ ДЛЯ RENDER (чтобы сервер не засыпал) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

@app.route('/health')
def health():
    return "OK"

def run_bot():
    bot.polling(non_stop=True)

if __name__ == '__main__':
    t = threading.Thread(target=run_bot)
    t.start()
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
