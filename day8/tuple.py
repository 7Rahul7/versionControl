
# Tuple is an immutable datatype in python

# Tuple can take different datatypes regardless they are mutable or immutable

# Indexing and Slicing in typle is same as that of list

# Tuple elements are enclosed with parenthesis i.e ()

# Creating an empty tuple

t = tuple()

t= ()

# Creating non = empty tuple

t = (1,1,1,[1,2,3])

print(t) # (1,1,1,[1,2,3])

# Accessing Tuple elements

#Tuple elements are accessed using indexing and slicing

vowels = ("a","e","i","o","u")

print(vowels[-1]) # u
print(vowels[0]) # a
print(vowels[3]) # o
# print(vowels[10]) # Error

data = ("a","b","c","d","e","f","g","h","i","j")

print(data[0:7]) #("a","b","c","d","e","f","g")
print(data[:5]) #('a', 'b', 'c', 'd', 'e')
print(data[6:]) #('g', 'h', 'i', 'j')
print(data[3:8]) #('d', 'e', 'f', 'g', 'h')
print(data[6:2]) #()
print(data[6:-2]) #('g', 'h')
print(data[-9:-2:2]) #('b','d','f','h')

