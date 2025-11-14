friends_last_Seen  = {
    "Alice": "2024-06-01 10:15:00",
    "Bob": "2024-06-01 11:20:00"
    }
print('dict before modification:',id(friends_last_Seen))
friends_last_Seen["Charlie"] = "2024-06-01 12:30:00"
print('dict after modification:', id(friends_last_Seen))
# The id remains the same, indicating the dictionary is mutable
ls = [1, 2, 3]
print('list before modification:',id(ls))
ls.append(4)
print('list after modification:',id(ls))
# The id remains the same, indicating the list is mutable

tp = (1, 2, 3)
print('tuple before modification:',id(tp))
tp += (4,)
print('tuple after modification:',id(tp))
# Tuples are immutable, so we cannot modify them directly.

x = 10
print('integer before modification:',id(x))
x += 5
print('integer after modification:',id(x))
# Integers are immutable, so a new object is created when we modify it.

nlist = [1, 2, 3]
print('list before modification:',id(nlist))
nlist+=[7,11]
print('list after modification:',id(nlist))
# The id remains the same, indicating the list is mutable