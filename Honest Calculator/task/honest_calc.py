# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0


def take_input():
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    x = check_number(x)
    y = check_number(y)
    check_oper(oper)
    if x is not None and y is not None:
        calculate(x, y, oper)


def check_number(n):
    try:
        if n == "M":
            return memory
        else:
            return float(n)
    except ValueError:
        print(msg_1)
        take_input()


def check_oper(o):
    if o not in ['+', '-', '*', '/']:
        print(msg_2)
        take_input()


def calculate(x, y, oper):
    if oper == '+':
        check(x, y, oper)
        print_result(float(x + y))
    elif oper == '-':
        check(x, y, oper)
        print_result(float(x - y))
    elif oper == '*':
        check(x, y, oper)
        print_result(float(x * y))
    elif oper == '/':
        check(x, y, oper)
        if y == 0:
            print(msg_3)
            take_input()
        else:
            print_result(float(x / y))


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (float(x) == 1.0 or float(y) == 1.0) and oper == "*":
        msg = msg + msg_7
    if (float(x) == 0.0 or float(y) == 0.0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    try:
        i = float(v)
        return i.is_integer() and i > -10 and v < 10
    except ValueError:
        return False


def print_result(result):
    ask_to_store(result)


def ask_to_store(result):
    print(result)
    print(msg_4)
    answer = input()
    if answer == "y":
        if is_one_digit(result):
            ask_if_sure(result)
        else:
            global memory
            memory = result
            ask_to_continue()
    elif answer == "n":
        ask_to_continue()
    else:
        ask_to_store(result)


def ask_if_sure(result, msg_index=10):
    print(globals()[f"msg_{msg_index}"])
    answer = input()
    if answer == "y":
        if msg_index < 12:
            msg_index += 1
            ask_if_sure(result, msg_index)
        else:
            global memory
            memory = result
            ask_to_continue()
    elif answer == "n":
        ask_to_continue()
    else:
        ask_if_sure(result, msg_index)


def ask_to_continue():
    print(msg_5)
    answer = input()
    if answer == "y":
        take_input()
    elif answer != "n":
        ask_to_continue()


take_input()
