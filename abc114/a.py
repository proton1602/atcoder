ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
INF = 10**18

X=ri()
if X==7 or X==5 or X==3:
    print('YES')
else:
    print('NO')