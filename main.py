from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from config import TOKEN
from calc import *
from menu import *
import random
# from play

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
calc_handler = CommandHandler('calc', calculator)
info_handler = CommandHandler('info', info_calc)
float_calculate_handler = CommandHandler('float', float_calculate)
complex_calculate_handler = CommandHandler('complex', complex_calculate)
play_handler = CommandHandler('play', play)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(float_calculate_handler)
dispatcher.add_handler(complex_calculate_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(play_handler)

print('server started')
updater.start_polling()
updater.idle()


