from datetime import datetime, timedelta
import time
from timeit import timeit
print(time.time())

# send email
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print(f"time taken { end - start}")

# datetime

d1 = datetime(2000, 1, 12)
d2 = datetime.now()

duration = d2 - d1
print(duration)
print(f"days: {duration.days}")
print(f"seconds: {duration.seconds}")
print(duration + timedelta(days=1, seconds=1000))
