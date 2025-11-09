short_tuple = (1, 2, 3)
print(short_tuple)
# short_tuple.append(4)  # This will raise an AttributeError since tuples are immutable
short_tuple = short_tuple + (4,)  # Creating a new tuple by concatenation
print(short_tuple)
print(short_tuple[0])  # Accessing element by index