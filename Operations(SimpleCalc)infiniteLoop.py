def cont():
    resp = input("Do you wish to continue?\n if yes please press 'Y' if not press 'N'")
    if resp == "n" or resp == "N":
        return False
    return True
while True:
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
    if not cont():
        break