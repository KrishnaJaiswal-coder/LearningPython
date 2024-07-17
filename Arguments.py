# 1)Default Argument example(values of parameters are defined itself in the given function)
def name(fname, mname="parsad", lname="shakya"):
    print("Hello,",fname,mname,lname,".Welcome to CBC company!")
name(fname="Krishna")

# 2)Keyword Argument Example(values are defined but we can change the order and value according to need)
def Average(a=3,b=4):
    avg= (a+b)/2
    print("The average of",a,"and",b,"is",avg,".")
Average(b=3,a=7)

# 3)Required Argument (The arguments whole value are not defined in function must be given by the user itself)
def Average(a,b):
    avg= (a+b)/2
    print("The average of",a,"and",b,"is",avg,".")
Average(b=8,a=7)

