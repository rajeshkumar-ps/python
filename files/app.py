my_file = open('files/data.txt', 'r') 
file_content = my_file.read()
print(file_content)
my_file.close()

my_file = open('files/data.txt', 'w') 
my_file.write('Rajesh')
my_file.close()