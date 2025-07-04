import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number from 0 to 9 guess the right answer!")
while playing:
    guess=input("give me your best guess!")
    if number==guess:
        print("you won the game!")
        print("the number is",number)
        break
    else:
        print("you lost try agin")