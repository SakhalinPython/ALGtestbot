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
    bot.send_message(message.chat.id, 'cc')

@bot.message_handler(content_types='text')
def my_text(message):
    if message.text.lower() == 'покажи список':
        bot.send_message(message.chat.id, '1) Команда 1 (qr) \n2) Команда 2 (mem)\n3) Команда 3 (txt)')
    if message.text.lower() == 'qr':
        bot.send_message(message.chat.id, 'Пиши команду qr и ссылку через пробел')
        bot.send_message(message.chat.id, 'qr Https://ya.ru/')
    elif message.text.lower() == 'mem':
        print('mem')
    elif message.text.lower() == 'txt':
        print('txt')

bot.infinity_polling()