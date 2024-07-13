import time
a=time.strftime('%H:%M:%S')
print(a)
h=int(time.strftime("%H"))
m=int(time.strftime("%M"))
s=int(time.strftime("%S"))
print(h)
print(m)
print(s)
if(h>=1 and h<12 and m<60 and s<60):
        print("Good morning.It is",a,"'O clock now.")  
elif(h>=12 and h<17 and m<60 and s<60):
        print("Good Afternoon.It is",a, ";O clock now.")
else:
    if(h>=17 and h<=24 and m<60 and s<60):
        print("Good evening.It is ",a,"'O clock now.")


# import time
# timestamp=int(time.strftime('%H'))
# print(timestamp)
# if(1<=timestamp<12):
#     print("Good Morning. The time is", timestamp,"'O clock now.")
# elif(12<=timestamp<17):
#      print("Good Afternoon. The time is", timestamp,"'O clock now.")
# else:
#       print("Good Evening. The time is", timestamp,"'O clock now.")
