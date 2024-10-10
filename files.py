import os 
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
#print(f.read())
#print(f.read(4))

# print(f.readline())
# print(f.readline(4))

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

#Append = create the file if it doesn't exixt

f = open("names.txt", "a")
f.write("\nMilan")
f.close()

# Write (overWrite)

f= open("context.txt", "w")
f.write("I deleted all of the context1")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways create a new file

# Opens a file for for writing, creates the file if it doesn't exist

f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists

if not os.path.exists("GGM.txt"):
    f = open("GGM.txt", "x")
    f.close() 

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("name_list.txt"):
    os.remove("name_list.txt")
else:
    print("The file you wish to delete doesn't exist")

# with has built-in implicit exception handling
# close() will be automatically called

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)

