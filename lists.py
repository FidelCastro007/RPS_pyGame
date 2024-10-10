# lists

grocery_list = ['apple', 'milk', 'brinjal']

data = ['GGM',18, True]

emptylist = []

print("apple" in grocery_list)

print(data[-1])
print(grocery_list.index("apple"))
print(grocery_list[:2])
print(grocery_list[-3:-1])

print(len(data))

grocery_list.append('orange')
print(grocery_list)

grocery_list += ['rice']
print(grocery_list)

print('')
grocery_list.extend(['fish', 'chicken'])
print(grocery_list)

print('')
grocery_list.extend(data)
print(grocery_list)

print('')
grocery_list.insert(0, 'Mutton')
print(grocery_list)

print('')
grocery_list.insert(2, 'pepper')
print(grocery_list)

print('')
grocery_list[1:3] = ['GGM', "mil"]
print(grocery_list)

print('')
grocery_list[2:2] = ["hello"] #slice
print(grocery_list)

print('')
grocery_list.remove(18)
print(grocery_list)

print('')
print(grocery_list.pop())
print(grocery_list)

print('')
del grocery_list[0]
print(grocery_list)

print('')
data.clear()
print(data)

print('')
grocery_list.sort()
print(grocery_list)

print('')
grocery_list[1:2] = ['Salt']
print(grocery_list)
grocery_list.sort()
print(grocery_list)

# grocery_list.append(18) //shows type error bcos of sort of list so must contains same vals (SORT)
print('')
grocery_list.sort(key=str.lower)
print(grocery_list)

nums = [3,2,78,1,5]
nums.reverse()
print(nums)

nums.sort()
print(nums) #Ascending

nums.sort(reverse=True) # Descending
print(nums)

nums = [1, 24, 48, 3, 5]
print(sorted(nums, reverse=True))
print(nums)

numscopy =nums.copy()
mynums = list(nums)
mycopy = nums[:]

print('')
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)
print(type(nums))

mylist = list([1, "GGM", True])
print(mylist)

#Tuples - immutable or unchangable

mytuple = tuple(("GGM_mil",42,True))
print(mytuple)
anotherTuple = (1,2,5,4,7)

print(type(mytuple))
print(type(anotherTuple))

newlist = list(mytuple)
newlist.append("hola")
newTuple = tuple(newlist)
print(newTuple)

(one, *two, hi) = anotherTuple #destructuring tuple

print(one)
print(*two)
print(hi)

print(anotherTuple.count(2))


