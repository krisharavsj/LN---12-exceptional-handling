try:
    number=int(input("please enter a number"))
    print("the entered number is",number)
except ValueError as ex:
    print("exception",ex)