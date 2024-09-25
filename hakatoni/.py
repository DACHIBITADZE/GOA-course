#for loopის საშუალებით დაპრინტეთ 5ის ჯერადი რიცხვები ნოლიდან ასამდე.
for i in range(0,101,5):
      print(i)


def calculator(num1, op, num2):
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("ERROR")
 
 
calculator(10, "*", 2)



