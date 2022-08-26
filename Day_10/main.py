# Beginner 

# Function with Output => docString

# def format_name(f_name, l_name):
#     """ documentation """
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# fomated_string = format_name(input("What is you first name? "),input("What is you last name? "))
# print(fomated_string)



# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
        
# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30 ,31, 30, 30, 31, 30, 31, 30]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]


# year = int(input("Which year do you want to check? "))
# month = int(input("Which month do you want to check? "))
# days = days_in_month(year, month)
# print(days)



# Calculator Project
from numpy import subtract


def add(n1, n2):
    return n1 + n2

def subract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+" : add, "-": subtract, "*" : multiply, "/" : divide}

def calculator():                                  
    """ Recursion """
    num_1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:    
        operation_symbol = input("Pick an operation: ")
        num_2 = float(input("What's the next number? "))
        calculation = operations[operation_symbol]
        answer = calculation(num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'no' to start a new calculation:") == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()

calculator()