ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,M=rl()
P=[0]*M
Y=[0]*M
dic = [[] for _ in range(N+1)]
for i in range(M):
    P[i],Y[i] = rl()
    dic[P[i]] += [Y[i]]

for i in range(N+1):
    dic[i].sort()

import bisect
for i in range(M):
    print("{:0>6}{:0>6}".format(P[i], bisect.bisect_left(dic[P[i]],Y[i])+1))
