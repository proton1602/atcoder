import sys
input = sys.stdin.readline
ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD=10**9+7

N,X=rl()
BLU = []
dif = 0
dif1 = 0
tk1 = 0
ans = 0
for i in range(N):
    b,l,u = rl()
    dif += b*l
    dif1 += b*u
    tk1 += X*u
    BLU.append([b,l,u])

BLU.sort(key=lambda x: (x[2],x[1],-x[0]), reverse=True)

for b,l,u in BLU:
    dif += b*(u-l)
    tk = X*u
    if dif <= tk:
        ans += (dif + (u-1)) // u
        break
    else:
        dif -= tk
        ans += X

for i in range(1,N+1):
    b,l,u=BLU[-i]


print(ans)