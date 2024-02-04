import telebot
from telebot import types
from random import choice
import qrcode
import datetime

token='5993558048:AAEwlZC5sc4eyFt9QgO1Js0Xgf9bmDoWRf0'

bot = telebot.TeleBot(token)
greetings = ['Hello', 'Привет!', 'Как дела?', 'Че по чем!']
users = dict()

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.from_user.id in users:
        pass
    else:
        users[message.from_user.id] = [message.from_user.first_name, message.chat.id]
    bot.send_message(message.chat.id, f"{message.from_user.first_name},"
                                      f" {choice(greetings)}")
    bot.send_message(message.chat.id, 'Доступные команды /time')

@bot.message_handler(commands=['time'])
def current_time(message):
    bot.send_message(message.chat.id, f'Твое время - {datetime.datetime.now()}')



bot.infinity_polling()
