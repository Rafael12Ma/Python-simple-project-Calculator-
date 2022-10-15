from turtle import *


# APLO KOMPIOUTERAKI
print("\nPinakas Epilogwn\n")
print("Press + for pros8esi\nPress - for afairesi\nPress * for pollaplasiasmo\nPress / for diairesh")

ep = input("\nEnter your choice : ")
num1 =float(input("enter first number: "))
num2 =float(input("enter second number: "))



def dev(num1, num2):
    return num1 / num2


def mult(num1, num2):
    return num1 * num2


def minus(num1, num2):
    res=num1-num2
    return res


def plus(num1, num2):
    return num1 + num2

if (ep == "/"):
    if (num2 != 0):
        print(dev(num1, num2))
    else:
        print("den ginetai diairesi me to 0")
elif (ep == "*"):
    print(mult(num1, num2))
elif (ep == "-"):
    print(minus(num1, num2))
elif (ep == "+"):
    print(plus(num1, num2))


