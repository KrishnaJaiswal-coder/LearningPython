#Strings are immutale i.e they cant be changed once value is assigned

a='Apple'
a1=a.upper()
a2=a.lower()
print("The upper case for",a,"is",a1)
print("The lower case for",a,"is",a2)

#rstrip(" ") (used for removing the trailing characters)

str='Hi Ram!!'
print(str.rstrip("!"))  

#replace(" "," ") (used to replace all occurences of a string with another string)
fruit='apple , banana , apple'
print(fruit.replace("apple","cat"))

# split(" ") (used to seperate the words seperated by space in the given string to form a list)
a3="!!apple Banana! Cat!!"
print(a3.split(" "))
 
#Capitalize( ) (it turns the first character to upper case and the rest of the char to the lower case)
heading="my fiRst Blog Written in Python. I love Python"
print(heading.capitalize( ))

# center(50) (used to align the string to the center)

b='Hello world'
print(b.center(50))

# count(" ") (counts the repetition of the value of in the string)
conv='Hi Ram. Hi Shyam'
print("The repetition of Hi in the string is", conv.count("Hi"),"times")

# endswith("") (to check if the given string ends with our required character or not)

h='Apple is a healthy fruit!'
print(h.endswith("!"))

h="Welcometotheconsole"
print(h.endswith("to", 4 , 10))

# find(" ") (used to find the index of first occurence of the given value in the string and if not found return -1 as O/P)
# index(" ") (used to find the index of first occurence of the given value in the string and if not found return error as O/P)
B='Hi my name is Krishna  and Krishna studies in class 10'
print(B.find("krishna"))

# isalnum( )( checks whether the string contains character from A-Z , a-z and 0-9)
a="Welcome00"
print(a.isalnum())
print(a.isalpha())

#isprintable (checks if all the character in the string are printable or nor and returns true or false accordingly)
a="Hello\tMadam"
a1=a.upper()
print(a.isprintable())
print(a1.isupper())

# isspace( ) ( checks if the string only contains the white space or not)
Q="             "
print(Q.isspace())

#istitle( ) (checks if each word in the string starts with Capital letter or not)
W="Hi My Name Is Krishna"
print(W.istitle())

# #startswith( )
O="Apple is my favouite fruit"
print(O.startswith("Apple"))

#swapcase( ) (Upper case <=> Lower case)
C="HelLo TherE"
print(C.swapcase())
