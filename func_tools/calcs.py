from func_tools.divide import divide 
from func_tools.sum import sum
from func_tools.subtruct import subtruct
from func_tools.multiply import multiply


def calcs():
    operation = input("""
    Please type in the match operation you would like to complete :
    + for summation
    - for subtraction
    * for multiplication
    / for division""")

while is_running:
    number_1 = int(input("Enter first number!"))
    number_2 = int(input("Enter second number!"))

    if operation == "+": 
        func_tools.sum(a, b)
    elif operation == "*": 
        func_tools.multiply(a, b)
    elif operation == "/": 
        func_tools.divide(a, b)
    else:
        print("you have not typed a valid operator, please run the program again")
        calculate()