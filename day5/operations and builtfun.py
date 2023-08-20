# # Concatenation (+)
# m1 = "Hello"
# m2 = "World"
# result = m1 + m2
# print(result)  # "HelloWorld"


# # Repetition / Broadcast (*)
# m1 = "Hello"
# result = m1 * 3
# print(result)  # "HelloHelloHello"


# # Membership Operation ('in' and 'not in')

# print("h" in "Hello")  # False
# print("e" in "Hello")  # True
# print("o" not in "Hello")  # False


# built in function
#len() gives the length of any sequential objects

a = "Hello"

print(len(a))

# type() it gives the datatypes of an object

print(type(a))


# slice() it takes start and end values

s= slice(2, 5)
a= "Hello"

print(a[s])



message = "hello world"

result = message.capitalize()
print(result)

# title
message = "hello world"

result = message.title()
print(result)

# upper
message = "hello world"

result = message.upper()
print(result)


# lower
message = "hello world"

result = message.lower()
print(result)


#split
message="Hello World"

result=message.split()
print(result)


message = "hello world"
result =message.split("o")
print(result)

# join()

data =['hell', ' w', 'rld']
result="o".join(data)
print(result)

data =['hello','world']
result= " ".join(data)
print(result)

# find()

message = "hello world"
result = message .find("o")
print(result)

#  if we give the subset not present in the string then find ( ) returns -1. eg

message = "hello world"
result = message .find("lde")
print(result)

#replace ()

message = "hello world"
result = message .replace("hello","HELLO")
print(result)