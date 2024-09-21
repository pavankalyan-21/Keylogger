# file handling

# writing a file
f = open("file.txt" , "w")
f.write("Hi there! How are you doing?")
f.close()

# reading a file
f = open("file.txt" , "r")
data = f.read()
print(data)
f.close()

# appending data to a file
f = open("file.txt" , "a")
f.write("\nMy name is Pavan Kalyan")
f.close()