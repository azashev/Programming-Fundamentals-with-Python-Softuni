# Write a program that reads the path to a file and subtracts the file name and its extension.

path = input().split("\\")
file_name, extension = path[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")
