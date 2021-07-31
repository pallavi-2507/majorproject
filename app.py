from telegram.ext import Updater, MessageHandler,Filters
def lighton(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://en.wikipedia.org/wiki/Centennial_Light#/media/File:Centennial-Light-Bulb-pendant-light-in-Livermore-CA-2016.jpg'
  bot.message.reply_text('turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text('My name is palvibts-Bot')

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "turn on the light":
    lighton(bot,update)
  elif a =="what is your name?" or a=="name please":
    demo2(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = '1934417703:AAE9ly_1YmEyWl3XlYS3V-z8GIBm2ThQRh4'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
from telegram.ext import Updater, MessageHandler,Filters
def lightoff(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://en.wikipedia.org/wiki/Edison_screw#/media/File:Gluehlampe_01_KMJ.jpg'
  bot.message.reply_text('turned off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text('My name is palvibts-Bot')

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "turn off the light":
    lightoff(bot,update)
  elif a =="what is your name?" or a=="name please":
    demo2(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = '1934417703:AAE9ly_1YmEyWl3XlYS3V-z8GIBm2ThQRh4'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
from telegram.ext import Updater, MessageHandler,Filters
def fanon(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Spinning_ceiling_fan.jpg'
  bot.message.reply_text('switched on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text('My name is palvibts-Bot')

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "switch on fan":
    fanon(bot,update)
  elif a =="what is your name?" or a=="name please":
    demo2(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = '1934417703:AAE9ly_1YmEyWl3XlYS3V-z8GIBm2ThQRh4'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
from telegram.ext import Updater, MessageHandler,Filters
def fanoff(bot,update):
  chat_id = bot.message.chat_id
  path ='https://commons.wikimedia.org/wiki/File:The_Black_Beauty.jpg'
  bot.message.reply_text('switched off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text('My name is palvibts-Bot')

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "switch off fan":
    fanoff(bot,update)
  elif a =="what is your name?" or a=="name please":
    demo2(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = '1934417703:AAE9ly_1YmEyWl3XlYS3V-z8GIBm2ThQRh4'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
