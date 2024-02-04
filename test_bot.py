# pip install pyTelegramBotAPI
# pip install qrcode

import telebot
from telebot import types
from random import choice
import qrcode

token='6026848306:AAGCBYZy95arx9LbUWzZ8ZtxlPL1rxflVjM'

bot=telebot.TeleBot(token)
greetings = ['Привет!', 'Как дела?', 'Вацап', 'Бон жур!']
image_urls = ['https://i.pinimg.com/736x/4f/87/56/4f875635ca282de2f683daf31ed0e91f.jpg',
              'https://i.pinimg.com/236x/fc/9b/6c/fc9b6c7f71f11b4fa15ad08ea2e717e4.jpg',
              'https://i.ytimg.com/vi/oFPxdL1vd-A/hqdefault.jpg']
bot_users = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, choice(greetings))
    bot.send_message(message.chat.id,'У нас есть комманды /start , /help , /qrcode, /who, /randimg')
    user_id = message.from_user.id
    user_nick = message.from_user.username
    bot_users.append((user_id, user_nick))
    bot.send_animation(message.chat.id, open('stupid-rat-pizza-tower.gif', 'rb'))

@bot.message_handler(commands=['randimg'])
def start_message(message):
    bot.send_message(message.chat.id,'Улыбнись!!')
    bot.send_photo(message.chat.id, choice(image_urls))

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет help')



@bot.message_handler(commands=['qrcode'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет qrcode')
    bot.send_message(message.chat.id,'Сделать код - qr и ссылка, например "qr Http://ya.ru/"')
    # qr = qrcode.QRCode()
    # qr.add_data('Какие-то данные')
    # img = qr.make_image()
    # img.save(f'{message.from_user.id}_test.png')
    # bot.send_photo(message.chat.id, open(f'{message.from_user.id}_test.png', 'rb'))

@bot.message_handler(commands=['who'])
def start_message(message):
    for id, name in bot_users:
        bot.send_message(message.chat.id, f'{id} - {name}')

@bot.message_handler(content_types='text')
def start_message(message):
    temp = message.text.split(" ")

    if message.text.lower() == 'картинка':
        bot.send_message(message.chat.id, 'Твоя картинка')
        bot.send_photo(message.chat.id, open('h1.jpg', 'rb'))
    elif message.text.lower() == 'мем':
        bot.send_message(message.chat.id, 'Твой мем')
        bot.send_video(message.chat.id, open('video_2024-01-14_14-09-10.mp4', 'rb'))
    elif temp[0].lower() == 'qr':
        bot.send_message(message.chat.id, f'Твоя ссылка - {temp[1]}')
        qr = qrcode.QRCode()
        qr.add_data(temp[1])
        img = qr.make_image()
        img.save(f'{message.from_user.id}_test.png')
        bot.send_photo(message.chat.id, open(f'{message.from_user.id}_test.png', 'rb'))

@bot.message_handler(content_types='voice')
def start_message(message):
    bot.send_message(message.chat.id, 'Вы прислали голосовое')
    data = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(data.file_path)
    with open(f'{message.from_user.username}_test.ogg', 'wb') as fl:
        fl.write(downloaded_file)


bot.infinity_polling()
