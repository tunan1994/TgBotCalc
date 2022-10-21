from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from operation import *
from random import randint
from uuid import uuid4


def put(update, context):
    """Usage: /put value"""
    # генерируем идентификатор
    key = str(uuid4())
    # Здесь не используется context.args, 
    # т.к. значение может содержать пробелы.
    value = update.message.text.partition(' ')[2]

    # сохраняем значение в контекст
    context.user_data[key] = value
    # отправляем ключ пользователю
    update.message.reply_text(key)

def get(update, context):
    """Usage: /get uuid"""
    # отделяем идентификатор от команды
    key = context.args[0]

    # загружаем значение и отправляем пользователю
    value = context.user_data.get(key, 'Not found')
    update.message.reply_text(value)


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 7: "))
    while x < 1 or x > 7:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f" {name} взял {k}, теперь у него {counter}. На столе осталось {value} конфет.")



counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл(а) {player1}, у него(неё) теперь {value+counter1+counter2} конфет")
else:
    print(f"Выиграл(а) {player2}, у него(неё) теперь {value+counter1+counter2} конфет")