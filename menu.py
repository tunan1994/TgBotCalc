from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from operation import *
import operation as oper


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
f""" Приветствую Дорогой {update.effective_user.first_name}
Ты находишься в моем тг боте.
У него есть 2 функции:
Калькулятор рац и компл чисел: /calc
И игра в кофетки: /play
Выбирай, смелее ;-) """)

def calculator(update, context):
    context.bot.send_message(update.effective_chat.id,
f""" Поздравляю {update.effective_user.first_name}
Ты выбрал калькулятор
рациональных и комплексных чисел.
Чтобы узнать как пользоваться
его функциями введи /info """)

def info_calc(update, context):
    context.bot.send_message(update.effective_chat.id, 
""" Чтобы выполнить арифметическое действия
воспользуйтесь следующими командами:
/float a + b,
/complex a+bj * c-dj
Команда, числа, и операторы отделяются пробелами""")

def play(update, context):
    context.bot.send_message(update.effective_chat.id,
f""" Поздравляю {update.effective_user.first_name}
Ты выбрал игру в конфетки
Правила очень просты:
каждый по очереди берет конфеты
кто заберет последние - тот выйграл 
~~ К сожаленю не довел игру до ума
времени катастрофически не хватает~~ """)

