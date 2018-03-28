
'''
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits[1:9])

test = fruits[:]
print(test)

test[len(test):]=['google', 'giff']
print(test)
print(len(test))

test[len(test)-1]='google2'
print(test)

test.append('google3')
print(test)

test.sort()
print(test)
'''

# List Comprehensions
squares = list(map(lambda x: x**2, range(10)))
print(squares)

cubes = [x**3 for x in range(10)]
print(cubes)

mixs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(mixs)

# Tuples
# A tuple consists of a number of values separated by commas
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking 
empty = ()
singleton = "hello",
t = 1234, 4321, 'Ehay!'  # this is called tuple packing
x, y, z = t              # this is called sequence unpacking
print(x)


# Sets
'''
A set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. 
Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b) # letters in a but not in b
print(a | b) # letters in a or b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both


# Dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
del tel['sape']
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
for k, v in tel.items():
    print(k,v)