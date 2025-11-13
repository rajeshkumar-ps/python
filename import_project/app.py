import utils.file_operation as fo # Importing the file_operation module within directories
fo.save_to_file('example.txt', 'Hello, World!') 
content = fo.read_from_file('example.txt')
print(content)  # Output: Hello, World!