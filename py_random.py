import string
import random

print(random.random())  # 0-1
for i in range(10):
    print(random.randint(1, 10))  # 1-10

# pick random from array
# print(random.choice([1, 2, 3, 4, 5]))
print("return single value from an arr ", random.choice([1, 2, 3, 4, 5]))
print("return 3 values ran from an arr", random.choices([2, 3, 4, 5], k=3))
# string module
# create password
password = random.choices(string.ascii_letters + string.digits, k=6)
print("Gene random pass:", "".join(password))
