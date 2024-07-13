#  If else statement is used to execute a code of block with two conditions and execute the only block of code which meets the requirement by checking the input

# a=int(input("Enter your age: "))
# if(a>=18):
#     print("He/She can vote.")
# else:
#     print("He/She cannot vote")

radius=int(input('Enter the radius of the circle:'))
if(radius>=1):
    area=3.14*radius**2
    print("The area of the circle is:", area)
else:
    print("Invalid Input.\"The radius must be a positive number\"")
