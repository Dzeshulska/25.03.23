from divide import divide
from sum import sum
from subtruct import subtruct
from multiply import multiply


def calcs(a,b,operation):
    if operation == "+": 
         sum.sum(a, b)
    elif operation == "-": 
         subtruct.subtruct(a, b)    
    elif operation == "*": 
        multiply.multiply(a, b)
    elif operation == "/": 
        divide.divide(a, b)
    else:
        print("you have not typed a valid operator, please run the program again")
a = int(input("Enter first number!"))
b = int(input("Enter second number!"))
operation = input("""
        Please type in the match operation you would like to complete :
        + for summation
        - for subtraction
        * for multiplication
        / for division""")

calcs(a,b,operation)