#lambda 
squared = lambda num : num * num
print(squared(2)) # lambda simplifies the func in easy way (eg: write a one big func but need to do some operations in this func so we go to small func and we call this small to one to this big for this operation instead of we use lambda)

add_two = lambda num : num + 2

print(add_two(5))
def add_two(num): return num + 2 # same as lamba above one
print(add_two(7))

sum_tottal = lambda a,b : a+b
print(sum_tottal(7,5))
print('')

def funcBuilder(x):
    return lambda num: num + x

add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(5))

nums = [3,5,7,12,18,20,21]

""" def squaredNums1(numsq):
    list1 = [num*num for num in numsq]
    return list1

Total_list=squaredNums1([3,5,7,12,18,20,21])
print(Total_list) """

squared_nums = map(lambda num:num*num,nums) # map two params first one func second one param but that one used in that funcof 1st param
print(list(squared_nums))

odd_nums = filter(lambda num: num % 2 != 0,nums)
print(list(odd_nums)) # it only show the true condition of vals & don't show the false condition vals

from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr,nums,5)
print(total)
print(sum(nums,7))

names = ['GGM',"Milan","Fidel"]

def charcaterTotal(char):
    char_total = [len(val) for val in char]
    return char_total
total = charcaterTotal(names)
print((total))

char_count = reduce(lambda acc, curr: acc + len(curr), names,0)
print(char_count)