num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
operation = input("Please choose Operation: \nA.Addition\nB.Subtraction\nC.Multiplication\nD.Division\n")
if operation == "A" or operation == "a":
    total = int(num1) + int(num2)
    print(str(num1) + " + " + str(num2) + " = " + str(total))
elif operation == "B" or operation == "b":
    total = int(num1) - int(num2)
    print(str(num1) + " - " + str(num2) + " = " + str(total))
elif operation == "C" or operation == "c":
    total = int(num1) * int(num2)
    print(str(num1) + " * " + str(num2) + " = " + str(total))
elif operation == "D" or operation == "d":
    total = int(num1) / int(num2)
    print(str(num1) + " / " + str(num2) + " = " + str(total))
else:
    print("Invalid Operation!")
