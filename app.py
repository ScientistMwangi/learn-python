from modules import sales
import modules.sub_module.test_modules


print("Hello")
# Strings
language = " Python programming "
# Get Immutable (primitive types are immutable) memory location
print(id(language))
print(language[0])
print(language[-2])
print(language[:])
# slice uses : takes start and end, last character is not included
print(language[0:3])
# String operations
print("String Methods")
print(language.title())
print(language.lower())
print(language.strip())
print(language.find("Py"))
print(language.replace("P", "-"))
print("Python" in language)
print("python" not in language)

# formatted string
fname = "Samuel"
lname = "Mwangi"
full = fname + " " + lname
print(full)
# Better way
full2 = f"{fname}  {lname}"
print(full2)

# inputs
user_input = 0  # input("Enter value : ")
res = int(user_input) + 10
# type conversion - stringly typed python
# bool(), int(), float(), str()
# Falsy
# bool("")
# bool(0)
# bool(None(null))
print(res)

age = 22
if age >= 18:
    print("Adult")
if age >= 13:
    print("Teen")
else:
    print("Child")

# Functions


def increment(num: int, step: int = 2) -> tuple:
    return (num, num + step)


print(increment(10))

# varibale number of args

print("Function with variable args")


def multiply(*list):
    total = 1
    for x in list:
        total *= x
    return total


print(multiply(1, 2, 3, 4, 5))


def fizz_buzz(number):
    message = str(number)
    if number % 3 == 0 and number % 5 == 0:
        message = "fizz buzz"
    elif(number % 3 == 0):
        message = "fizz"
    elif number % 5 == 0:
        message = "buzz"
    print(message)


fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(11)

# packing
print()
print("Packing")

sales.calc_shipping()
modules.sub_module.test_modules.test()
print()
print()
