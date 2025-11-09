#set don't hold order and they dont allow duplicate values
art_friends = {'rajesh','amrita','priti'}
art_friends.add('sneha') #// adds an element to the set
print(art_friends)
science_friends = {'rajesh','amrita','sneha'}
#comparison
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)
print(art_friends.intersection(science_friends))
print(art_friends.union(science_friends))

a = {1, 2, 3, 4}
b = {4,3,1,2}
print((a==b))