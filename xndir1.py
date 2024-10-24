num1 = int(input("first number "))
num2 = int(input("second number "))
operation = input("choose operation + - * /  ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("please choose avilable operation")
print(result)


