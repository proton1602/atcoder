N,K=map(int,input().split())
A=list(map(int,input().split()))

b_len = len(format(max(A),'b'))
B = [[int(_) for _ in format(a, '0{}b'.format(b_len))] for a in A]
B_t = [list(b) for b in zip(*B)]
B_b = [int(sum(b)<=(N/2)) for b in B_t]
K_b = [int(_) for _ in bin(K)[2:]]


if len(K_b) > len(B_b):
    B_b = K_b[:(len(K_b)-len(B_b))] + B_b
else:
    K_b = [0]*(len(B_b)-len(K_b)) + K_b
import copy
x_b = copy.copy(B_b)
for i in range(len(K_b)):
    if B_b[i] == 0 and K_b[i] == 1:
        break
    elif B_b[i] == 1 and K_b[i] == 0:
        x_b[i] = 0

from functools import reduce

x = int(reduce(lambda x,y:x+y, [str(a) for a in x_b]), 2)

ans = sum(x^a for a in A)
print(ans)
