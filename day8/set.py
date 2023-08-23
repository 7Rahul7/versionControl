
# Set is a mutable datatype in python. But, the elements of the set must be immutable

# Unlike list, set is unordered. So, indexing and slicing is not possible in Python

# In set {1,2} is equal to {2,1}

# Creating an empty set 
s= set()
# s= {} This is not an empty set. It is an empty dictionary  

# Creating a non-empty set

s={1,1.2,(1,2),True}

s1 = set([1,2,3,4,4,3,2,1])

print(s1) # {1,2,3}

# s={1,[1,2],3} #this is invalid set because it has list as an element whic is mutable
# s={1,2,(1,2,[3,4])} # this is also invalid because tuple has a mutable element


