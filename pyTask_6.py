#Read - r
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")

#Append - a
with open('example.txt', 'a') as file:
    file.write("\nThis is a new line appended to the file.")
print("Content appended to the file.")

#Write - w
with open('example.txt', 'w') as file:
    file.write("This content will replace the existing content.")
print("File written with new content.")

#Create - x
try:
    with open('newfile.txt', 'x') as file:
        file.write("This is a new file created using the 'x' mode.")
    print("File created and written to.")
except FileExistsError:
    print("The file already exists.")
