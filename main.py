import os
import telebot
my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey, how's it going?!")

bot.polling()


