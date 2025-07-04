import random
while True:
    user_action = input("enter a choice(rock =,paper,scissor)")
    possible_action=["rock","paper","scissor"]
    computer_actions=random.choice(possible_action)
    print(f"\n you chose{user_action},computer chose{computer_actions}")
    if user_action==computer_actions:
        print("its a tie!")
    elif user_action=="rock":
        if computer_actions=="scissor":
            print("you win!")
        else: 
            print("you lost")
    elif user_action=="scissor":
        if computer_actions=="paper":
            print("you won!")
        else:
            print ("you lost")
    elif user_action=="paper":
        if computer_actions=="rock":
            print("you won")
        else:
            print("you lost")
    play_again=input("play again?(y/n)")
    if play_again!="y":
        break