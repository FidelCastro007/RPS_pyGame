#Dictionaries

car = {  # obj in JavaScript
    "brand": "Tesla",
    "model": "Model_3_P",
    "year": 2024
}

car2 = dict(brand="Tesla", model="Model_3")

print(car)
print(car2)
print(len(car2))
print(type(car2))

#Access items

print(car["brand"])
print(car.get("model"))

# list all keys
print(car.keys())

# list all values 
print(car.values())

# list of key/value pairs as tuples
print(car.items())

# verify a key exists
print("model" in car)
print("price" in car)

#Change values
car["brand"] = "Nio"
car.update({"price": 10007})

print('')
print(car)

# Remove items
print(car.pop("price")) # // removes last val and shows the removed val only
print('')
print(car)

car["Ev"] = "yes"
print(car)

print(car.popitem()) # // removes that last val but it shows both key & val
print('')

print(car)

# Delete and clear

car["Ev"] = "yes"
print(car)
del car["Ev"]
print(car)

print(car2)
car2.clear()
print(car2)

del car2 # removes the full dictionary with curly braces also
# print(car2)

# Copy dictionaries

car2 = car # create a reference (using same resources but diff name) note: if you change the val of any Copyvar(dict) it changes in both not in one var(dict) !!

print('')
print("Bad Copy!")
print(car)
print(car2)
print('')

""" car2["Ev"] = "no"

print(car) #bad copy
print(car2) """

car2 = car.copy()

car["Ev"] ="No" # key & val
print('')
print("Good Copy!")
print(car)
print(car2)

# or use the dict() constructor func

car3 = dict(car)
print('')
print("GOOD Copy!")
print(car3)

# Nested dictionaries 

member1 = {
    "name": "page",
    "instrument": "brand"
}

member2 = {
    "name": "Plant,ggm",
    "instrument": "model","name": "ggm1"
    #"name":"GGM" // keys should be unique in dictionary & duplicate key value can't repeated but it can replace the val of original (Strictly AVOIDED)
}
band = {
    "member1": member1, #reusing the dictionaries key & vals
    "member2": member2
}
print('')
print(band)
print(band["member1"]["name"]) # relatively 2d array concept in javascript

# Sets

nums1 = {1,2,5,7}

nums2 = set((1,2,7,5))

print(nums1)
print(nums2)
print(type(nums1))
print(len(nums1))

# No duplicate allowed in Sets

nums2 = {1,2,2,3}
print(nums2)

# True is a dupe of 1, False is a dupe of Zero

nums = {True,1,2,False,3,4,0}
print(nums)

# check if a value is in a set 
print(2 in nums)

# but you cannot refer to  an element in the set with an index position or a key

# Add a new element to a set 

nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1,2,3}
two = {2,3,4}

#one way of intersect
one.intersection_update(two) # straight away update the set without variable or values
print(one)

# Aother way of intersect
print('')
intersect = one.intersection(two)
print(intersect)

# Keep everything except the duplicates

one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one) 

