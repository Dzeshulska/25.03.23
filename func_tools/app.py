from func_tools.divide import divide
from func_tools.sum import sum
from func_tools.subtruct import subtruct
from func_tools.multiply import multiply

while is_running :
    user_choose = input("Do you want to work with calc? y/n : ")

    if user_choose == "y":
        num1 = input()
        num2 = input()
    elif user_choose == "n":
        is_running = False
    else :
        continue