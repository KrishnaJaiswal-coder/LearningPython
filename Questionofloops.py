# WAP to print the multiplication table of any number using loop statement
a=int(input("enter a number whole multiplication table is to be printed:"))
i=1
while (i<11):
    print(a,"*",i,"is",a*i,'\n')
    i=i+1
    
#WAP to print the elements of the list [1,4,9,16,25,36,49,64,81,100] using loop
nums=  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx=0
while idx < len(nums):
    print(nums[idx],end=",")
    idx+=1

