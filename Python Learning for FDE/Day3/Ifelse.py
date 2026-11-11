age = int(input("Enter your age : "))

if age>=18:
    print("Congratulations,You are eligible to vote")
else:
    print("Sorry,You are Not eligible to vote")

n=int(input("Enter a number : "))

if n>0:
    print(n,"It is a positive number")
elif n<0:
    print(n,"It is a negative number")
else :
    print("Zero")

print("Odd or Even")
n1=int(input("Enter your number"))
if (n1%2==0):
    print("Even Number")
else:
    print("Odd Number")

print("Grade Calculator")
marks = int(input("Enter your marks"))
if marks>=90 and marks<=100:
    print("A+")
elif marks>=80 and marks<=89:
    print("A")
elif marks>=70 and marks<=79:
    print("B")
elif marks>=60 and marks<=69:
    print("C")
elif marks>=50 and  marks<=59:
    print("D")
elif marks<50:
    print("Fail")
else:
    print("Enter a valid mark please")