print("test")

# comments line

a: int = 3
print(a)

print(type(a))

Str = "this is string"
print(Str)

print("value of a is", a)

a = "string1"
b = "string2"
print(a,"concat",b)
print(a+"concat"+b)

values = [1, 2, "rahul", 4, 3]

# print list values by index
print(values[0])
print(values[3])
print(values[-1]) # prints last index values
print(values[1:3]) # prints index 1, 2

# inserting values
values.insert(3, "shetty")
print(values)

# Inserting values at the end
values.append("end")
print(values)

# updating existing values
values[2] = "RAHUL123"
print(values)

# deleting existing values
del values[0]
print(values)

# 1
# 4
# 3
# [2, 'rahul']
# [1, 2, 'rahul', 'shetty', 4, 3]
# [1, 2, 'rahul', 'shetty', 4, 3, 'end']
# [1, 2, 'RAHUL123', 'shetty', 4, 3, 'end']
# [2, 'RAHUL123', 'shetty', 4, 3, 'end']

# tuple
tuple1 = (1, 2, 'rahul', 4, 3)
print(tuple1)

# dictionary
dict = {1:"sadik", 2:"shaik", "empId":"2434675"}
print(dict)
print(dict["empId"])
print(dict[1])

# Create empty dictionary, pass values for a empty dictionary
dict2 = {}
dict2["firstname"] = "shaik"
dict2["second name"] = "Sadik"
dict2['gender'] = "M"
print(dict2)

# IF block

greeting = "Good Morning"

if greeting == "Morning":
    print("condition matches")
    print("second line of if loop")
else:
    print("not matching")
    print("2nd line of else loop")

print("outside if else")

# For loop

# iterate the values of list
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)

# Sum of first 5 natural numbers
# iterate a range of values
sum1 = 0
for j in range(1, 6): # range will be 1 to 5
        sum1 = sum1 + j
print(sum1)

# jump with iteration count
for k in range(1, 10, 2):
    print(k)

# not mentioning the initial index
for k in range(10):
    print(k) # prints 0 to 9 (not 1 to 10)

# While loop
# to check a condition, if the condition is true it will keep on executing the loop
# for loop - we have fixed iteration number, While loop - it is based on condition is true

i = 4
while i>1:
    print(i)
    i = i - 1
# above code prints 4, 3, 2

# multiple loops
i = 4
while i>1:
    if i != 3:
        print(i)
    i = i - 1
# above code prints 4, 2


# break keyword - comes out of while loop
i = 10
while i>1:
    if i == 3:
        break
    print(i)
    i = i - 1
# above code prints 10 to 4

print("latest")
# continue keyword - It skips the next steps of current iteration of while loop, directly goes to next iteration
# Break keyword - it comes out of while loop
i = 10
while i > 1:
    if i == 9:
        i = i - 1
        continue
    if i == 3:
        break
    print(i)
    i = i - 1


# ****************** Functions ************************

def GreetMe():
    print("good morning")

GreetMe()

# *****************************************************
def GreetMe1(name):
    print("good morning",name)

GreetMe1("Sadik")

# *******************************************************

def addIntegers(a,b):
    print(a+b)

addIntegers(2,5)

# *******************************************************
def addIntegers1(a, b):
    c = a + b
    return c
print(addIntegers1(7, 8))

# *************************** OOPS ***************************

class Calculator:

    num = 100 # class variables, common for all objects

    # default constructor
    def __init__(self):
        print("inside constructor")

    # methods inside class
    def getData(self):  # "self" is mandatory for methods inside class
        print("method inside class")

    #def summation(self):


obj = Calculator()  # syntax for creating object in python, It should be outside class
obj.getData()
print(obj.num)








