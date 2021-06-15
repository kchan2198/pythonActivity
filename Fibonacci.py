num = int(input())
num1 = 0
num2 = 1
num3 = 0

while num3 < num:
    print(num1)
    hold = num1 + num2
    num1 = num2
    num2 = hold
    num3 += 1