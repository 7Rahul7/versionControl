# sort(key,reverse) 

# sort method can take two parameters key and reverse
# reverse take boolean type and key takes a function

# data =[1,23,53,65,21,32,43]
# result = data.sort()
# print(data)

# # for reverse 
# data.sort(reverse=True)

# data =["ram","hero","Aoole"]

# data.sort()


# data =[(12,13),(15,53),(67,21),(89,98)]

# def get_second_element(element):
#     return element[1]


# data.sort(key=get_second_element)
# print(data)


# task
a =[(4,12,5),(6,1),(11,12),(6,7,8)]

def task (element):
    return element[-1]

a.sort(key=task)

print(a)