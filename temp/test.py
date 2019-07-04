import time 
import random

N = 100000
st = time.time()
aa = []
for i in range(N):
    a = [random.randint(0,10000) for _ in range(4)]
    aa += [a]
en = time.time()
print("+= []: ", en-st, "[s]")

st = time.time()
aa = []
for i in range(N):
    a = [random.randint(0,10000) for _ in range(4)]
    aa = aa + [a]
en = time.time()
print("= + []: ", en-st, "[s]")

st = time.time()
aa = []
for i in range(N):
    a = [random.randint(0,10000) for _ in range(4)]
    aa.append(a)
en = time.time()
print("append: ", en-st, "[s]")

st = time.time()
aa = []
for i in range(N):
    a = [random.randint(0,10000) for _ in range(4)]
    aa.extend([a])
en = time.time()
print("extend: ", en-st, "[s]")