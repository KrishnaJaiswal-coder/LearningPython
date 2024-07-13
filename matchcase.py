a=int(input("Enter the value of the first number: "))
b=int(input("Enter the value of the  second number: "))
x=(input("enter '+' for addition\t '-' for subtraction\t '*' for multiplication and '/' for divison of the numbers: "))
match x:
    case '+':
        sum=a+b
        print("The sum of",a,"and", b , "is", sum)
    case '-':
        subtraction= a-b
        print("The difference of",a,"and", b , "is", subtraction)
    case '*':
        Multiplication=a*b
        print("The product of",a,"and", b , "is", Multiplication)
    case '/':
        Division=a//b
        print("The division of",a,"and", b , "is", Division)
    case _:
        print("Invalid Input")
 

