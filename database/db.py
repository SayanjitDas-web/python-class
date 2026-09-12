from uuid import uuid4

DFL = "./database/db.txt"

def create_db():
    with open(DFL,"w") as file:
        return "file created successfully"
    file.close()
    
def add_data(data):
    with open(DFL,"a") as file:
        file.write(str(uuid4())+" "+data+"\n")
        file.close()
        
def delete_data(id):
    data = []
    with open(DFL,"r") as file:
        data = file.readlines()
        file.close()
        
    target = ""
    for line in data:
        if id == line.split(" ")[0]:
            target = line
    
    data.remove(target)
            
    with open(DFL,"w") as file:
        file.write("")
        file.close()
        
    with open(DFL,"a") as file:
        for line in data:
            file.write(line)
        file.close()
        
def get_data(id):
    target = ""
    with open(DFL,"r") as file:
        for line in file.readlines():
            if id == line.split(" ")[0]:
                target = line
        file.close()
        
    return target

def update_data(id,newData):
    data = []
    with open(DFL,"r") as file:
        data = file.readlines()
        file.close()
        
    target = ""
    for line in data:
        if id == line.split(" ")[0]:
            target = line
            
    target_index = data.index(target)
    data[target_index] = id+" "+newData+"\n"
    
    with open(DFL,"w") as file:
        file.write("")
        file.close()
        
    with open(DFL,"a") as file:
        for line in data:
            file.write(line)
        file.close()
        
def get_all_data():
    data = []
    with open(DFL,"r") as file:
        data = file.readlines()
        file.close()
    return data