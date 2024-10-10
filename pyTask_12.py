# 10 Common Exceptions in python

lst = [1, 2, 3]
print(lst[3])  # Raises IndexError

my_dict = {"a": 1, "b": 2}
print(my_dict["c"])  # Raises KeyError

int("abc")  # Raises ValueError

1 + "2"  # Raises TypeError

5 / 0  # Raises ZeroDivisionError

my_list = [1, 2, 3]
my_list.add(4)  # Raises AttributeError

with open('non_existent_file.txt', 'r') as f:  # Raises FileNotFoundError
    data = f.read()

import non_existent_module  # Raises ImportError

print(non_existent_variable)  # Raises NameError

my_iter = iter([1, 2])
next(my_iter)
next(my_iter)
next(my_iter)  # Raises StopIteration
