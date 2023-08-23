# Dictionary are the mutable datatypes in Python
# They are the key value pairs enclosed within curly braces

# creating a empty dictionary

a = {}
print(a)

a = dict()
print(a)

# Creating non-empty dictionary

student= {"name":"jane","age":30,"address":"KTM"}
student = dict(name="Jane",age=30,address = "KTM")

print(student)

# Accessing elements of a dictionary

# Dictionary elements are accessed using keys

student=dict(name="Jane",age=30,address = "KTM")
name = student ["name"]

print(name)

age = student["age"]

print(age)

address = student["address"]
print(address)

# print(student["roll_no"]) this throws key error
 
# Accessing dictionary elements using .get() method

student =dict(name="Jane",age=30,address = "KTM")

name = student.get("name")
print(name)

roll_no = student.get("roll_no")
print(roll_no)