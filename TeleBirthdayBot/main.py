import os
import telebot
from replit import db
import datetime
import time
import random
import keep_alive

def wishBday(person):
  ways=["Oii!, it's "+person+"'s birthday today","Guess who's birthday is today? It's "+person,]
  r=int(random.random()*2)
  return ways[r]





my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

keep_alive.keep_alive()

@bot.message_handler(commands=['remind'])
def greet(message):
  while(1):
    today = datetime.date.today()
    val= today.month+0.01*today.day
    for person in db.keys():
      if db[person] == val:
        bot.send_message(message.chat.id, wishBday(person))
    time.sleep(86400)
    
    # bot.send_message(message.chat.id, db.keys())

bot.polling()
