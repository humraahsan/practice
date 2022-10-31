from art import calculator_logo

"""
first_num = int(input("What's the first number?: "))
operators = {"+" : add, "-" : sub, "*" : mul, "/": div}
for operator in operators:
    print(operator, "\n")
operation = input("Pick an operation: ")
next_num = int(input("What's the next number?: "))


def calculator(num1, num2):
    if operation == "+":
        return num1 +num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "%":
        return num1 % num2
    else:
        return print("Invalid operator")


print(calculator(first_num, next_num))

"""


# Calculator


# add
def add(n1, n2):
    return n1 + n2


# sub
def sub(n1, n2):
    return n1 - n2


# Mul

def mul(n1, n2):
    return n1 * n2


# Div

def div(n1, n2):
    return n1 / n2


def calculator():
    print(calculator_logo)
    num1 = float(input("What's the first number?: "))
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    for operator in operators:
        print(operator, "\n")
    cal_finished = False
    while not cal_finished:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calling_func = operators[operation]
        result = calling_func(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation \n") == 'y':
            num1 = result
        else:
            cal_finished = True
            calculator()

calculator()
