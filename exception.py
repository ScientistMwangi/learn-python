from timeit import timeit
# string conversion to integer
# program crashes as the exception was not handled
from decimal import DivisionByZero
from tokenize import Number


print("No Exception handled - program crashes")
age = int(input("Age: "))
print(f"your age is: {age}")

print()
print("Exception handled")
try:
    # file = open("app.py")
    # object with enter and exit method can clean up themselves i.e like using in C#,
    # called context manage protocol
    # with open("app.py") as file, open("dest.txt") as target => this code does not need cleanup
    age = int(input("Age: "))
    print(f"your age is: {age}")
except (ValueError, ZeroDivisionError):
    print("age cannot be zerro")
finally:
    # excuted always good for clean up like closing files
    # file.close()
    print("Finally block do some clean up here")


print()
print("Raising Exception")


def cal_test_function(age):
    if(age <= 0):
        raise ValueError("Age cannot be Zero or less")
    return 10 / age


# Test above function
# problem with the above we still have to use try and except
try:
    cal_test_function(0)
except (DivisionByZero, ValueError):
    print("age cannot be zero or less")

# Rasing exception is costly especially when the code will be executed several times 10,000+
# if you can handle the code in a better way just do

print()
print()
code1 = """"
def cal_test_function(age):
    if(age <= 0):
        raise ValueError("Age cannot be Zero or less")
    return 10 / age

try:
    cal_test_function(0)
except (DivisionByZero, ValueError):
    pass
"""

code2 = """"
def cal_test_function_no_raised_execption(age):
    if(age <= 0):
        return None
    return 10 / age


res = cal_test_function_no_raised_execption(0)
if res == None:
    print("code to be timed")
"""
# print("First code with raise: ", timeit(code1, number=10000))
print("Second code NO raise: ", timeit(code2, number=10000))
