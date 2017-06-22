# -*- coding: utf-8 -*-

"""
file_id's
 1 - AwADAgADXAADRrRJSi3lmjAPwpayAg
 2 - AwADAgADXQADRrRJSotbToaI4L43Ag
 3 - AwADAgADXgADRrRJSr9VK46hijFEAg
 4 - AwADAgADXwADRrRJSgVdWCC0c1hfAg
 5 - AwADAgADYAADRrRJSkqBm8KONaciAg
"""

import config
import telebot
import os
import time

bot = telebot.TeleBot(config.token)

# при комманде /test, отправляем на сервер Телеги наши файлы
# и получаем их file_id
@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            #Отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id = msg.message_id)
        time.sleep(3)

if __name__ == '__main__':
    bot.polling(none_stop=True)