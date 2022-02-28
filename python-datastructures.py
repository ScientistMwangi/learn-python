from ast import Expression
from collections import deque
from array import array
from operator import contains
from pkgutil import iter_modules


letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(zeros)
combined = letters + zeros
print(combined)

numbers = list(range(10, 20, 2))
print(numbers)

char = list("samuel mwangi")
print(char)

print(numbers[::2])
# Steps also works as reverse if you use ::-1
print(numbers[::-1])
# unpacking list
first, *other, last = numbers
print(first)
print(other)
print(last)

# loop and enumerate
for letter in letters:
    print(letter)
for letter in enumerate(letters):
    index, value = letter
    print(index, value)
# better
for index, value in enumerate(letters):
    comb = f"index: {index} value: {value}"
    print(comb)

# Add items
surname = list("kibuika")
surname.append("z")
print(surname)
# insert at specific position
surname.insert(1, "1")
print(surname)
# delete
# remove only one character - loop if need to remove everything
# surname.remove("k")
# end
# surname.pop()  # default remove the last, also pass an index
# surname.pop(-2)
# remove multiple
del surname[0:3]  # remove first 3

print(surname)
# clear- remove everything
# surname.clear()
print(surname)
# Find in alist
print(surname.count("k"))
print(surname.index("k"))
# Get index of something does not exist get error in python other lan -1
if "k" in surname:
    print(surname.index("k"))

# sorting
nums = [5, 51, 7, 10]
# sorted function create anew sorted list
print(sorted(nums, reverse=True))
# nums.sort(), does not create a new list
nums.sort()
print(nums)
# sorting more complicated objects
products = [("product1", 10), ("product2", 13), ("product3", 4), ]

# first  use a function


def sort_item(item):
    return item[1]


# products.sort(key=sort_item)
print(products)

products.sort(key=lambda item: item[1])
print(products)

# map function
items = [("product1", 10), ("product2", 13), ("product3", 4), ]
ids = list(map(lambda item: item[1], items))
print("get only ids: ", ids)

filtered_list = filter(lambda item: item[1] >= 10, items)
print(list(filtered_list))

# comprehesion
print("comprehesion")
print([item[1] for item in items])
# Only items with id <=10
res2 = [item for item in items if item[1] >= 10]
print("Id greator than 10 ", res2)
# stack - implemented using list
print("stacks using list")
print()
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
if stack:
    print(stack.pop())
    print(stack)
if stack:
    print(stack[-1])
    print(stack)
print()

# queue - have to import queue from collection

q = deque([])
q.append(1)
q.append(2)
q.append(3)
if q:
    print(q.popleft())
    print(q)
if q:
    print(q[0])
    print(q)

# array like list just that they have a type
# offer better performace than list huge value +10,000

arr = array("i", [1, 2, 3, 4])
print(arr[0])
arr.remove(3)
print(arr)

# set , no duplicate, {}, union, intersection etc, cannot use index
first = set([1, 2, 2, 4, 5, 6, 7])
print(first)
second = {1, 5, 8, 9}
print(first | second)
print(first & second)
if 1 in first:
    print(1)

# dictionary
print()
print("Dictionary")
dic1 = {"x": 1, "y": 2}
dic2 = dict(x=1, y=2)
dic2["w"] = 10
print(dic2)

# delete
del dic2["y"]
print(dic2)

dic2["s"] = "samuel"
print(dic2)

if "s" in dic2:
    print("if condition or use get", dic2["s"])
print(dic2.get("s"))

# iterate
for key in dic2:
    print(key, dic2[key])
print()
print("Loop using dic2.items() => returns a tuple")
print()
for item in dic2.items():
    print(item[0], item[1])
# Dictionary comprehesion
# set
set_values = {x for x in range(5)}
print(set_values)
print(type(set_values))
# dictionary
dic_value = {}
dic = {x: x for x in range(6)}
print(dic)


# Excercise most repeated character

def most_repeated_char(sentence):
    sentence = sentence.replace(" ", '')
    chars = [*sentence]
    dicOfChars = {}
    res3 = ["0", 0]
    for c in chars:
        if c in dicOfChars:
            dicOfChars[c] += 1
        else:
            dicOfChars[c] = 1
        if(dicOfChars[c] > res3[1]):
            res3[0] = c
            res3[1] = dicOfChars[c]
            print(f"c: {c}: count: {dicOfChars[c]}")
    print(res3)
    print(dicOfChars)


print()
print("Excercise")
sentence = "This is a common interview question"
most_repeated_char(sentence)
