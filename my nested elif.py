# # It is used to apply conditions within the condition

# a=int(input('Enter any number:'))
# if(a<0):
#     print("The number", a,"is a negative integer.")
# elif(a>0):
#     if(a>=1 and a<=10):
#         print("The number",a, "lies in between 1 and 10.")
#     elif(a>10 and a<=20):
#         print('The number",a, "lies in between 11 and 20.')
#     else:
#         print('The number',a,"is greater than 20.")
# else:
#     print('The number is',a)

# WAP to print the greeting according to the time given by the user

Time=float(input("What time it is now:"))
# AP=int(input("Enter 1 for Am and 2 for Pm:"))
if(Time>=1 and Time<12):
    # if(AP==1):
        print("Good Morning Everyone.It is",int(Time),"'O clock now.Have a nice day ahead!")
elif(Time>=12 and Time<=24):
    if( Time>=12 and Time<=17):
        print("Good Afternoon Everyone. How is your day going on!")
    elif(Time>17 and Time<24):
        print("Good Evening Everyone. How was your day?")
else:
    print("Invalid input.")
     