# String data type


# literal assignment

first_name = "GGM"
last_name = "Subscribe"

print(type(first_name))
print(type(first_name) == str)
print(isinstance(first_name, str))

# constructor function

name = str ("CLick the sus button")

print(type(name))
print(type(name) == str)
print(isinstance(name, str))

#Concatenation
full_name = first_name +" "+ last_name +"!"
print(full_name)

#Casting a number to str
decade = str(1989)
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

multi_line = '''
hi welcome
        if you want sub to my
                    GGM Channel 
'''
print(multi_line)

sentence = 'pleaseee\' support as \t and share it \n like it❤'
print(sentence)

print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.replace('pleaseee',"subcribe"))

print(len(sentence))

sentence += "  " 
sentence = "    " + sentence 
print(len(sentence))
print(sentence)
print(len(sentence.strip())) # it removes empty spaces from Left side and right side only
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$4".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String Index Value
first = "Subscribe"
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("S"))
print(first.endswith("e"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa * -1)) #absolute val

print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
print(zipcode)
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incoorect data
# zip_value = int("New York")

#User Input

a = input("Subscribe to ggm: \n")
print(a)








 
