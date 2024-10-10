# Write a python program to create a set

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)


# Write a python program to iterate over sets

# Iterating over a set
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)


# write a python program to odd elemets to a set

# Adding elements to a set
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
print("Set after adding elements:", my_set)


#write a python program to remove item from a give set

# Removing an item from a set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Will raise an error if the item is not in the set
print("Set after removing an element:", my_set)



# write a python program to remove an item from a set it is present in the set

# Safely removing an item if it's present in the set
my_set = {1, 2, 3, 4, 5}
my_set.discard(6)  # Will not raise an error if the item is not in the set
print("Set after discarding:", my_set)



# write a python program to create an intersection of sets

# Creating an intersection of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)


# write a python program to create a union of sets

# Creating a union of two sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union = set1.union(set2)
print("Union of sets:", union)


""" # Adding odd elements to a set
my_set = set()

# Adding odd numbers between 1 and 10
for num in range(1, 11):
    if num % 2 != 0:  # Check if the number is odd
        my_set.add(num)

print("Set with odd elements:", my_set)
 """