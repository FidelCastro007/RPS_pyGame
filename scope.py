# SCope

name = "GGM" # global Varible
age1 = 21

# greeting("Sub") // local scope function
# print(name)

def another():
    print('')
    age = 27 #global_val in func
    global age1 # we don't declare this global term this comes "UnboundLocalError: cannot access local variable 'age1' where it is not associated with a value"
    age1 += 1
    color = 'green'
    def greeting(name):
        ages = 23 # local variable 
        print(age)
        print(ages)
        print(age1)
        print(name)
        nonlocal color #global vals can be modified by this nonlocal so local vals can't be accesed so only global be modified(SIMPLY GLOBAL VAR VALS DON"T WORK ONLY LOCAL VAR VALS WORS NOTE: VAR HAS SAME IN BOTH LOCAL & GLOBAL)
        color = 'red'
        print(color)
    greeting("Like")

another()

# CLosure is a function having access to the scope of its parent function has returned.

def parent_function(person, coins):
    #coins =3 

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins ==1:
            print("\n" + person + " has " +str(coins)+ " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game #func reference to its parent

tommy = parent_function("milan",5) # func calling

jenny = parent_function("GGM",4)

tommy()
tommy()

jenny()
tommy()

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

print(times3(7))
print(times5(5))
print(times3(4))
print(times5(times3(4)))

# f-strings

person = "GGM_Milan"
coins = 5

###########
#Concatenating strings

print("\n" + person + " has " + str(coins) + " coins left.")

##########
# Previous %s formatting

message = "\n%s has %s coins left" % (person,coins)
print(message)

#########
# Previous string.format() method

message = "\n{} has {} coins left.".format(person,coins)
print(message)

message = "\n{1} has {0} coins left.".format(person,coins)
print(message)


message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person
)
print(message)

player = {'person': "GGM", 'coins':7}

message ="\n{person} has {coins} coins left.".format(**player)
print(message)

###########
# f-strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {5 * 7} coins left."
print(message)

message =f"\n{player['person']} has {2*7} coins left."
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") #:.2f means controlling last 2 decimal vals after point(.)

for num in range(1 ,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range (1, 11):
    print(f"{num} divided by 4.57 is {num / 4.57:.2%}") # f means fixed, % means percentage