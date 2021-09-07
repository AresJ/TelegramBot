import os
import telebot
import yfinance as yf
my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey, how's it going?!")

@bot.message_handler(commands=['hello?'])
def hello(message):
  bot.send_message(message.chat.id, "Hey.")

@bot.message_handler(commands=['wsb'] or ['WSB'])
def getStocks(message):
    response = ""
    stocks = ['gme', 'amc', 'nok']
    stockData = []
    for stock in stocks:
      data = yf.download(tickers = stock, period='2d', interval='1d')
      data = data.reset_index()
      response += f"----{stock}----\n"
      stockData.append([stock])
      columns=['stock']
      for index, row in data.iterrows():
        stockPosition = len(stockData) - 1
        price = round(row['Close'], 2)
        formatDate = row['date'].strftime('%m %d')
        response += f"{formatDate}: {price} \n"
        stockData[stockPosition].append(price)
        columns.append(formatDate)
      print()

  response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
  for row in stockData:
    response += f"{row:[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
  response += "\nStock Data"
  print(response)
  bot.send_message(message.chat.id, response) 
        
bot.polling()


