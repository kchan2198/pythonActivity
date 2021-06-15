Name = input("Please enter your name: ")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = a+b+c+d
FinalGrade = e/4

if 98 <= FinalGrade <= 100:
    print("Congratulations " + Name + " with the Average of " + str(FinalGrade) + " with Highest Honors.")
elif 95 <= FinalGrade <= 97:
    print("Congratulations " + Name + " with the Average of " + str(FinalGrade) + " with High Honors.")
elif 90 <= FinalGrade <= 94:
    print("Congratulations " + Name + " with the Average of " + str(FinalGrade) + " with Honors.")
elif 75 <= FinalGrade <= 89:
    print("Congratulations " + Name + " with the Average of " + str(FinalGrade) + " You passed.")
elif 51 <= FinalGrade <= 74:
    print("FAILED!")
else:
    print("Invalid Grade")