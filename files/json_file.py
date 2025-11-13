import json
file = open('files/json_file.txt', 'r')
data = json.load(file)
file.close()
print(data['friends'][0])
