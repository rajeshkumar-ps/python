friends = ['rajesh','amrita']
friends.append('priti') #// append adds an element to the end of the list
print(friends)
friends.remove('priti') #// removes an element from the list
print(friends)
print([0,1,2]+[3,4,5])

comma_separated = ",".join(friends)
print(comma_separated)

#slicing list

# list comprehension 

lower_name = [name.lower() for name in friends]
print(lower_name)