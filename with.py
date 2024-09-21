# 'with' keyword 
# automatically release resources after use

# writing 
with open("with.txt" , "w") as f:
    f.write("Wow! You are so beautiful.")
# appending to the file
with open("with.txt" , "a") as f:
    f.write("\nYou are really gorgeous!")
# reading the file
with open("with.txt" , "r") as f:
    data = f.read()
    print(data)