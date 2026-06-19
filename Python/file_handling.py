# """ Starting to learn file handling in python """
# # opening a file
# with open("test.txt", 'w', encoding='utf-8') as file:
#     file.write("Hello, this is a test file.\n")
#     file.write("This file is used to demonstrate file handling in Python.\n")
#     file.write("We can write multiple lines to the file.\n")

# print("File has been written successfully.")

# with open("test.txt", 'a', encoding='utf-8') as file:
#     file.write("This line is appended to the file.\n")

# print("Line has been appended successfully.")

# with open("test.txt", 'r', encoding='utf-8') as file:
#     content = file.read()
#     print("Content of the file:")
#     print(content)

with open("students.csv", "w", encoding='utf-8') as file:
    file.write("name, age, gpa\n")
    file.write("Punj,19,9.8\n")
    file.write("Raghav,20,8.7\n")
    file.write("Alice,21,9.1\n")

with open("students.csv", "r", encoding='utf-8') as file:
    print("Name of the Students above 9 gpa is:")
    next(file)
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        gpa = float(parts[2])
        if gpa > 9.0:
            print(name)
