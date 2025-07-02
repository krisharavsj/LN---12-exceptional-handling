try:
    numb1,numb2=int(input("please enter 2 numbers seperated by commas"))
    result=numb1/numb2
    print("result is",result)
except ZeroDivisionError:
    print("zero division error")
except SyntaxError:
    print("SYNTAX ERROR")
except:
    print("wrong subject")
else:
    print("no exceptions")
finally:
    print("this will excecute no matter what")