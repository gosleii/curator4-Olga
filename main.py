import telebot

bot = telebot.TeleBot('6342685007:AAHhJt6PXKFV8hyGPZb6_WKGCn1Y7qVkBfk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'Убегай!! \nУбегай!!')


bot.infinity_polling()