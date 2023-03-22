from divide import divide
from sum import sum
from subtruct import subtruct
from multiply import multiply

is_running = True

while is_running :
    user_choose = input("Do you want to work with calc? y/n : ")

    if user_choose == "y":
        num1 = input()
        num2 = input()
    elif user_choose == "n":
        is_running = False
    else :
        continue