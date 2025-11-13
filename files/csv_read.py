file = open('files/csv_data.txt', 'r')
lines = file.readlines()
file.close()
lines = [line.strip() for line in lines[1:] ] # skip header and strip whitespace
for line in lines:
    name, age, university, degree = line.split(',')
    print('#'.join(line.split(',')))
    print(f'Name: {name.title()}, Age: {age}, University: {university.capitalize()}, Degree: {degree}')
    
