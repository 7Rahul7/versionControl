# dictionary values can be of any data type
# But, there is a rule for dictionary keys that they must be immutable.
# Dictionary keys cannot contain any mutable type directly or indirectly

data = {1:"Hello",2:"World"} #Valid

data = {2.1:[1,2,3], True:"Hello"} #Valid

data = {(1,2,3):1,(4,5):2} # Valid

data = {([1,2,3],2):"Hello", 2:"World"} # Invalid

data = {[1,2,3]:"Hello",2:"World"} #Invalid

data = dict(name="Jane",age=30,address = "KTM") #Valid

# Membership in Dictionary is observed in keys and not in values

student = {"name":"Jane","age":30,"address" : "KTM"}

print("Jon" in student) #false
print("name" in student) #true




