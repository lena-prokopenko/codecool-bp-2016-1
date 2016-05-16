
operation = input("Enter operation: ")
x = int(input("Enter your first number or LETTER to EXIT: "))

y = (input("Enter your second number: "))

if operation == "*":
    result = x * y
    print(result)

elif operation == "/":
    result = x / y
    print(result)
    try:
         exec(result)
    except ZeroDivisionError:
        print("Can't divide by zero")



elif operation == "+":
    result = x + y
    print(result)

elif operation == "-":
    result = x - y
    print(result)
else:
    exit()

print("Result: ", result)
