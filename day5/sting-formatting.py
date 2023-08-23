# String formatting in Python can be done with three methods
# 1.f-string
# 2.format specifier
# 3.format() method


# f-string

name = 'Jon'
message = f"Hello I'm {name}"

print (message)

# .format () method

name = "Jane"
language = "Python"
message = "Hello I'm {}. I'm learning {}".format(name, language)

print(message)

# format specifier

name = "Jon"
language = "Python"
age = 19

message = "Hello I'm  %s. I'm learning %s. I'm %d years old" % (
    name, language, age)

print(message)
