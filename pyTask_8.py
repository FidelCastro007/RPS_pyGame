#write a program to sum all items in a list

def sumOfItemsInList (itemSum):
    if not all(isinstance(num, int) for num in itemSum):
        return
    """  list1 = 0
    for num in itemSum:
        list1 += num
    return list1
 """
    return sum(itemSum) #equal to above code

sumItems = sumOfItemsInList([3,5,7,12,18,20,21])
print(sumItems)


# write a program to multiply all the items in a list
def mulOfItemsInList (itemMul):
    if not all(isinstance(num, int) for num in itemMul):
        return
    total = 1
    for num in itemMul:
        total *= num
    return total

mulItems = mulOfItemsInList([3,5,7,12,18,20,21])
print(mulItems)

# write a program to get the largest number of a list
# Function to find the largest number in a list
def find_largest_number(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers = [10, 25, 5, 76, 30]
largest_number = find_largest_number(numbers)
print("The largest number is:", largest_number)


# write a program to get the smallest number of a list
def find_smallest_number(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

# Example usage
numbers = [10, 25, 5, 76, 30]
smallest_number = find_smallest_number(numbers)
print("The smallest number is:", smallest_number)

# write a program to remove duplicates from a list
# method 1
def remove_duplicates(items):
    unique_items = []
    for item in items:
        if item not in unique_items: # membership operator
            unique_items.append(item) # join in single element
    return unique_items

# Example usage
items = [10, "apple", 25, "apple", 10, 76, "banana", 25]
unique_items = remove_duplicates(items)
print("List without duplicates:", unique_items)

# method 2
def remove_duplicates(numbers):
    return list(set(numbers))

# Example usage
numbers = [10, 25, 10, 76, 30, 25] # It doesn't care about index😅
unique_numbers = remove_duplicates(numbers)
print("List without duplicates:", unique_numbers)

# write a program to check if a list is empty or not
def is_list_empty(items):
    return len(items) == 0

# Example usage
items = []
if is_list_empty(items):
    print("The list is empty")
else:
    print("The list is not empty")
