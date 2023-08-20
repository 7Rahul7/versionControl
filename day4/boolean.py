# True and False are boolean of python and also keywords

# boolean type operation

# a=2
# b=3 
# c=4

# print(b>a) #true
# print(b!=a) #true 

# print(b> a and b==a) #not true
# print(b> a or b==a) #True
# print(b> a or b==a) #True

# print(not True) #false
# print(not False) #True

# print(not a) #false


# print( 2 in (1,2,3)) #true
# print( 2 in (1,5,3)) #false




a = 1 
b=1 
print(a is b) #true

a=1234567891
b=1234567891

#if data more than it is false
print(a is b) 


# concept of Truthy and Falsy

# Truthy

# All datatypes and number ,if non-empty and non-zero respectively are truthy values

# bool function is used to check truthy values
# Truthy
# All non-empty datatypes and non-zero numbers are truthy values
a = 12
b = 5.7
c = [1, 2]
d = (4, 5)
e = {1, 2}
f = {"name": "Jon"}
g = True
# All these datatypes are truthy datatypes
# We can check the truthiness of the data using bool function

print(bool(b))  # True





# Falsy
# All empty datatypes and zero are falsy values
a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = False
h = None
print(bool(b))

# python boolean are the subclass of integer class (tinyint) i.e 1= true,0=false


