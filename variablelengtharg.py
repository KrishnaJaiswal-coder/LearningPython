#Varibale Length Arguments are used when we need more arguments than that are acutally passed in thr function or 
# we dont know the exact numbers of parameters to be passed in the function.This can be acheived by two ways.One is
# 1)Arbitary Argument Example:
def average (*numbers):
    print(type(numbers))
    print(len(numbers))
    sum=0
    for i in numbers:
        sum=sum + i
    print("The average is", sum/len(numbers))
average(4,5,6,6)

#2)Keyword Arbitary Arguments (takes the argument as a dictionary)

def Name(**name):
    print(type(Name))
    print("Hello",name["fname"],name["mname"], name["Lname"],".Your id is",name["id"])
Name(fname="Krishna",Lname="Jaiswal",mname="kumar", id="07123")