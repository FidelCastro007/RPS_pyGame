# Functions
def hello_world():
    print("Hello World")

hello_world()

def sum(num1, num2=7):
    if (type(num1) is not int or type(num2) is not int):
        return 
    return num1+num2

total = sum(5)
print(total)

def multiple_items(*args): # *args means you can send many arguments
    print(args)
    print(type(args))

multiple_items("GGM","Mil","Fidel")

def add(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)

add(2,7,5,4,1)

def mult_named_items(**kwargs): # kwargs means key word argumnets
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Subcribe",last="Share",middle="like") # keywords in this case known as variables.It seems like vals joins with var

def func(a,b,*args,option = False,**kwargs):
    print("")
    print(a,b)
    print(args)
    print(option)
    print(kwargs)

func(1,3,10,220,Name = "GGM",salary= 70000)

# Recursion 

def add_one(num):

    if(num >=9):
        return num +1
    
    total = num + 1
    print(total)

    return add_one(total) # function calling itself 

myNewTotal = add_one(0)
print(myNewTotal)

#Program to print factorial of a number 
# recursively

def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n * recursive_factorial(n-1)
    
# user input
num = 7

# check if the input is valid or not
if num < 0:
    print("Invalid input ! Please enter a postive number.")
elif num == 0:
    print("Factorial of number 0 is 1")
else:
    print("Factorial of number", num, "=", recursive_factorial(num))

