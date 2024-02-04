import telebot
from telebot import types
from random import choice
import qrcode

token='ВАШ ТОКЕН'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, choice("Привет"))
    bot.send_message(message.chat.id,'У нас есть комманды /start , /help , /qrcode, /who, /randimg')

bot.infinity_polling()
