""" Starting to learn file handling in python """
# opening a file
with open("test.txt", 'w', encoding='utf-8') as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file is used to demonstrate file handling in Python.\n")
    file.write("We can write multiple lines to the file.\n")

print("File has been written successfully.")
