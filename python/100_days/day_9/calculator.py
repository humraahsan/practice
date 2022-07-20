""""
first_num = int(input("What's the first number?: "))
operators = {"+" : add, "-" : sub, "*" : mul, "/": div}
for operator in operators:
    print(operator, "\n")
operation = input("Pick an operation: ")
next_num = int(input("What's the next number?: "))


def calculator(num1, num2):
    if operation == "+":
        return num1 + num2
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


operations = {"+": add, "-": sub, "*": mul, "/": div}
