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

def float_calculate(update, context):
    arg = context.args
   
    a = float(arg[0])
    operator = arg[1]
    b = float(arg[2])
    if operator == '*':
        result = oper.mult(a, b)
    elif operator == '/':
        if b == 0:
            result = 'Деление на ноль невозможно'
        else:    
            result = oper.div(a, b)
    elif operator == '+':
        result = oper.sum(a, b)
    elif operator == '-':
        result = oper.diff(a, b)

    context.bot.send_message(update.effective_chat.id, f"Ответ на выражение {a}{operator}{b} = {result}")

def complex_calculate(update, context):
    arg = context.args

    a = complex(arg[0])
    operator = arg[1]
    b = complex(arg[2])
    if operator == '*':
        result = oper.mult(a, b)
    elif operator == '/':
        result = oper.div(a, b)
    elif operator == '+':
        result = oper.sum(a, b)
    elif operator == '-':
        result = oper.diff(a, b)

    context.bot.send_message(update.effective_chat.id, f"Ответ на выражение {a}{operator}{b} = {result}")