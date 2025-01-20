"""Create a List, tuple and Dictionary with 5 elements in it and, 
how to access few elements based on the index. Try  with different examples """

# List
lst = [10, 20, 30, 40, 50]
print("List:", lst)
print("Access element at index 2:", lst[2])
print("Slice elements from index 1 to 3:", lst[1:4])

# Tuple
tpl = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print("\nTuple:", tpl)
print("Access element at index 4:", tpl[4])
print("Slice elements from index 0 to 2:", tpl[0:3])

# Dictionary
dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("\nDictionary:", dct)
print("Access value for key 'c':", dct['c'])
print("Access value for key 'e':", dct['e'])