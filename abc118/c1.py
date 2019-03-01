N = int(input())
A = [int(i) for i in input().split()]

import math
import itertools

m = min(A)

for v in itertools.combinations(A,2):
    m1 = math.gcd(*v)
    if m > m1:
        m = m1
print(m)