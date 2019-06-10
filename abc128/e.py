import sys
input = sys.stdin.readline
ri = lambda: int(input())
rl = lambda: [int(x) if x.isdecimal() else x for x in input().split()]
rl = lambda: map(int, input().split())
rr = lambda N: [list(l) for l in zip(*[rl() for _ in range(N)])]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7


N,Q=rl()
TT = []
now = set()
for _ in range(N):
    s,t,x = rl()
    TT.append((s-x-0.5,1,x))
    TT.append((t-x-0.5,-1,x))
for i in range(Q):
    d = ri()
    TT.append((d,0,i))


TT.sort()
mx = INF
mx_f = False
ans = [-1]*Q
for st,w,x in TT:
    if w > 0:
        now.add(x)
        if mx > x:
            mx = x
            mx_f = True
    elif w < 0:
        now.remove(x)
        if mx == x:
            mx_f = False
    elif len(now) > 0:
        if not mx_f:
            mx = min(now)
            mx_f = True
        ans[x] = mx
print(*ans,sep='\n')