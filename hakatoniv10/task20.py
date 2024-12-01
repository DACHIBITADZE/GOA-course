num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))

math_doing = input("enter task you want to do: ")

if math_doing == "+":
    print(num1 + num2)
elif math_doing == "-":
    print(num1 - num2)
elif math_doing == "*":
    print(num1 * num2)
elif math_doing == "/":
    print(num1 / num2)
else:
    print("you chose wrong task")