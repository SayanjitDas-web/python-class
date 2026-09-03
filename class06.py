data = [11,22,33,44,55]

# for i in range(5):
#     print(data[i])

# for item in data:
#     print(item)

data[2] = 66
data.append(77)
data.append(88)
data.append(99)
data.pop()
data.pop(4)
print(data)

student = {
    "name":"Sayanjit",
    "roll":12,
    "age":24,
    "isPresent":False
}

# student["roll"] = 11
student.update({"roll":7})

del student["age"]

print(student)