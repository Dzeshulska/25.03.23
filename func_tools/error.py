try:
   user_choose = input("Do you want to work with calc? y/n : ")
except SyntaxError:
   raise SyntaxError("You must enter a small letter!")
else: 
   print("All right")