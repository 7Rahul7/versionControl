# Union
s1={1,2,3,4}
s2={3,4,5,6}

result = s1.union(s1)

print(result)

#or

print(s1 | s2)

# Intersection

result= s1.intersection(s2)

print(result)

#or

print(s1 & s2)

# Difference ()

result = s1.difference(s2)

print(result)

#or

print(s1 - s2)

# issubset() & issuperset()

s1 = {1,2,3,4,5,6}
s2 = {3,4,5,6}


print(s1.issubset(s2)) #False
print(s2.issubset(s1)) #True
print(s2.issuperset(s1)) #True
print(s1.issuperset(s2)) #False




#symmetric_difference ()

s1 ={1,2,3,4}
s2 ={3,4,5,6}

result = s1.symmetric_difference(s2)

print(result) #{1,2,5,6}

#or

print(s1 ^ s2)

# symmetric_difference_update()

s1.symmetric_difference_update(s2)

print(s1)

