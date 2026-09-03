# def add():
#     print(1+2)
    
def subs():
    print(2-1)
    
def calculate(num1,num2,op):
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("please give a operation argument")
        
calculate(11,10,"+")

add = lambda num1,num2 : print(num1+num2)

add(1,2)

def test():
    return "test passed"
    
# def test():
#     print("test passed")