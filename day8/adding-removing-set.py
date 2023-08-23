

# We have different methods to add and remove items in a set

# add()

s={1,2,3}

result = s.add(4)

print(result) #None

print(s)

#update

s.update([4,5,6])

print(s) #{1,2,3,4,5,6}

# discard()

s.discard(6) #discard() takes element as an argument
print(s) #{1,2,3,6,5}


#remove()

s.remove(4)

print(s) 

s.remove(10) #It throws error