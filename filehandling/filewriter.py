# Creating newfile.txt 
name = "ACF"
with open("newfile1.txt", 'w') as file:
    file.write(f"Hello, {name}!\n")
    file.write("Isn't this amazing?\n")
    file.write("That we can create and write on text files\n")
    file.write("using Python.")

# Creating newfile2.txt 
with open("newfile2.txt", 'w') as file2:
    file2.write("This message was created using Python.")

