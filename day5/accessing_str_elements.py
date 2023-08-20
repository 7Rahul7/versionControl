# we can access string elements using indexing and slicing which is similar to list
# forward indexing starts from 0 and reverse indexing from -1


# indexing
message = "Hello world"
# print(message[1])
# print(message[-20]) error
# print(message[-1])
# print(message[20]) error


# slicing
message = "I am learning python today"

# print(message[:6])  # I am l
# print(message[0:5])
# print(message[3:8])
# print(message[-8:-2])
print(message[2:8:2])  # empty
# print(message[4:])
# print(message[:6])


# message = "hello"
# message[2] ="L" #it is not possible because string is immutable
# print(message)


# del message #delete is an keyword that deletes the object
