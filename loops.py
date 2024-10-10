# loops
# While loop

i = 0
while i < 6:
    i += 1
    if i == 3 :
        continue
    print(i)
else:
    print("i is no longer lessthan 10")

# For loop
fruits = ["apple","banana", "mango"]

for x in fruits: #lists
    if x == "banana":
        continue
    print(x)

print('')
for x in "Share":
    print(x)

for x in range(10):
    print(x)

print('')
for x in range(4,7):
    print(x)

for x in range(0,101,5): # last val param as increment
    print(x)
else:
    print("Glad that\'s over!")

    names = ["GGM","Mil","Hola"]
    actions = ["Codes","eats","sleeps"]

for name in names:
    for action in actions:
        print(name + " "+ action + ".")

for action in actions:
    for name in names:
        print(name + " "+ action + ".")