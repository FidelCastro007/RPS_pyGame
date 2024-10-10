# program to create a tuple with different datatypes
my_tuple = ("Hello", 3.14, 10, True)
print(my_tuple)


# program to create a tuple with numbers and print one item
num_tuple = (1, 2, 3, 4, 5)
print(num_tuple[1])

# program to unpack a tuple in a several variables
my_tuple = ("Python", 42, 3.14)

# Unpacking the tuple into variables
lang, age, pi_value = my_tuple

print(lang)
print(age)
print(pi_value)

# program to addItem in a tuple

# Initial tuple
my_tuple = (1, 2, 3)

# Convert to list, add an item, and convert back to tuple
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)

# Printing the modified tuple
print(my_tuple)

# program to get 5th element from a tuple and also the 5th element from the last

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

# Getting the 5th element (index 4 since index starts at 0)
fifth_element = my_tuple[4]

# Getting the 5th element from the last
fifth_from_last = my_tuple[-5]

print("5th element:", fifth_element)
print("5th element from last:", fifth_from_last)


# program to find repeated element in a tuple

# Creating a tuple with repeated elements
my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 3)

seen = set()  # Initialize an empty set to track seen elements

# Finding repeated elements
repeated_elements = tuple(item*item for item in my_tuple
                           if my_tuple.count(item) > 1
                           and item not in seen
                           and not seen.add(item)) # we forget to give not it always give empty because first item encounter problem occurs

# Printing the repeated elements
print("Repeated elements:", repeated_elements)

# Method 2
# Creating a tuple with repeated elements
my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 3)

# Initialize a list to track processed items
processed = []

# Find repeated elements and store their squares, ensuring each is processed only once
repeated_elements = tuple(item*item for item in my_tuple 
                         if my_tuple.count(item) > 1 
                         and item not in processed 
                         and processed.append(item) is None)

# Print the repeated elements
print("Repeated elements:", repeated_elements)


""" # Creating a tuple with repeated elements
my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 3)

# Finding repeated elements while preserving order and eliminating duplicates
seen = set()  # Step 1: Initialize an empty set to track seen elements

# Step 2: List comprehension to process each item in the tuple
repeated_elements = [item*item for item in my_tuple 
                     if my_tuple.count(item) > 1   # Condition 1: item must be repeated (count > 1)
                     and item not in seen          # Condition 2: item must not have been seen before
                     and not seen.add(item)]       # Step 3: Add the item to 'seen' and return False to satisfy 'and'

# Printing the repeated elements
print("Repeated elements:", repeated_elements) """

