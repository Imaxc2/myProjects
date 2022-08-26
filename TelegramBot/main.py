import telebot
from bs4 import BeautifulSoup as BS
import requests
import time
import webbrowser

bot = telebot.TeleBot('5151583155:AAF63Mi2lUS4waQ2H5NehXX3dEJ0Swgc5xY')
waiturl = False


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    global waiturl
    ans = message.text.lower()
    if waiturl:
        waiturl = False
        bot.send_message(message.chat.id, 'Начинаю', parse_mode='html')
        while True:
            minim = 100000
            allcost = []
            r = requests.get(ans)
            html = BS(r.content, "html.parser")
            for el in html.select('.tc-price'):
                price = el.get_text()
                price = price.replace('Цена', '')
                price = price.replace('₽', '')
                price = price.replace('\n', '').strip()
                if price:
                    allcost.append(float(price.replace(' ', '')))
            for i in allcost:
                if i < minim:
                    minim = i
            bot.send_message(message.chat.id, f'{minim} \nСсылка: {ans}', parse_mode='html')

            time.sleep(60)
    elif ans == 'hello' or ans == 'привет':
        bot.send_message(message.chat.id, 'Привет!!!', parse_mode='html')
    elif ans == 'парсер' or ans == 'parser':
        waiturl = True
        bot.send_message(message.chat.id, 'Отправляй', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Напиши парсер чтобы парсер funpay начал работать, а потом дай ссылку.',
                         parse_mode='html')


bot.polling(none_stop=True, interval=0)
