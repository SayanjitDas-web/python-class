import math
from database.db import add_data, get_all_data, delete_data, update_data

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
        
while True:
    print("""
          enter 'a' for adding data
          enter 'd' for deleteing a data
          enter 's' for see all data
          enter 'u' for update a data
          enter 'e' for exit
    """)
    op = input("enter a option -> ")
    print()
    if op == "a":
        data = input("enter your data -> ")
        add_data(data)
    elif op == "d":
        id = input("enter the id -> ")
        delete_data(id)
    elif op == "u":
        id = input("enter the id -> ")
        newData = input("enter the new data -> ")
        update_data(id,newData)
    elif op == "s":
        for data in get_all_data():
            print(data)
    elif op == "e":
        break
    else:
        print("please select an option!")