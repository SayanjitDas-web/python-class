# Arithmetic Operators -> +,-,*,/,%,//,**
# Comparision Operator -> ==,!=,>,<,>=,<=
# Logical Operator -> and,or,not
# Asignment Operator -> =,+=,-=,*=,/=
# Membership Operator -> in, not in
# Identity Operator -> is, is not

# matching = True
# print(not matching)

# width = int(input("enter width: "))
# height = int(input("enter height: "))

# print("area of a rectangle is ",width*height)


num1 = 20
num2 = 20

# if (num1 > num2):
#     print("number1 is greater than number2")
# else:
#     print("number1 is not greater than number2")
    
    
# print("num1 is greater than num2") if(num1 > num2) else print("num1 is not greater than num2")

if(num1 > num2):
    print("num1 is greater than num2")
elif(num2 > num1):
    print("num2 is greater than num1")
else:
    print("both are equal")
    
    
print("num1 is greater than num2") if(num1 > num2) else(print("num2 is greater than num1") if(num2 > num1) else print("both are equal"))

age = 17

status = "Adult" if age >= 18 else "Minor"

print(status)

number = int(input("enter a number: "))

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
    
if number > 0:
    print("positive number")
elif number < 0:
    print("negative number")
else:
    print("number is zero")