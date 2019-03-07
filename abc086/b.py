ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

a,b = rl()

c = int(str(a)+str(b))
c_ = int(c**0.5)

if c==c_*c_:
    print('Yes')
else:
    print('No')
