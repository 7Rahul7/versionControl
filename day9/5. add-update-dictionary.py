
# ADD
student= dict(name="Jane",age=30,address = "KTM")
student["roll_no"] =21
print(student)

# UPDATE

student["name"] ="Jon"
print(student)

other_info = dict(institute="boardway",phone_no = 9876724553)

student.update(other_info)

print(student)

student.update(last_name="ABC")
print(student)