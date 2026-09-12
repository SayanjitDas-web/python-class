import math
from database.db import add_data, get_all_data

def render_table():
    for i in range(len(get_all_data()[0])+2):
        print("_",end="")
    print()
    print("|",end="")
    for i in range((math.floor(len(get_all_data()[0].split(" ")[0])/2))):
        print(" ",end="")
    print("ID",end="")
    for i in range((math.floor(len(get_all_data()[0].split(" ")[0])/2))):
            print(" ",end="")
    print("|")
    for i in range(len(get_all_data()[0])+2):
            print("`",end="")
    print()
    for data in get_all_data():
        print(data)
        
render_table()