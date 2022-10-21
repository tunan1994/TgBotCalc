from commands import *

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