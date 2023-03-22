def calculator(a,b,operation):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a/b
    else:
        print("Unsupportet operation")
    if result is not None:
        print("Result: ", result)

a = int(input("First number: "))

b = int(input("Second number: "))

operation = input("Operation: ")

calculator(a,b,operation)



