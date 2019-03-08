ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
F=[rl() for _ in range(N)]
P=[rl() for _ in range(N)]
ans = -INF

import itertools
for d in itertools.product(range(2),repeat=10):
    if sum(d) == 0: continue
    res = 0
    for i in range(N):
        res += P[i][sum(map(lambda x,y:x&y, F[i], d))]
    ans = max(ans,res)

print(ans)