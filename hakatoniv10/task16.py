secretnum = 7
num = int(input("please enter number to guess:"))

while num != 7:
    print("Try again")
    break
    num = int(input())
while num == 7:
    print("Congrats. you guessed the number.")
    break
# "შექმენით number guess თამაში. 
#description: შექმენით ცვლადი და მიანიჭეთ რაიმე int მნიშვნელობა. შექმენით მეორე ცვლადი რომელშიც მომხმარებელს შემოატანინებთ რაიმე რიცხვს. სანამ არ გამოიცნობს რა რიცხვი იყო პირველ ცვლადში, 
#დაუწერეთ: ""Try again"" თუ გამოიცნობს მაშინ: ""Congrats. You guessed the number"". (გამოიყენეთ while loop'ი)"												