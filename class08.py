import math
target = 7

# with open("test.txt","a") as file:
#     for i in range(1,11):
#         file.write(f"{i} X {target} = {i*target}\n")
#     file.write("-------\n")
#     file.close()

with open("test.txt","r") as file:
    for line in file.readlines()[4:10]:
        print(line.split(" ")[:math.floor(len(line.split(" "))/2)])
    file.close()