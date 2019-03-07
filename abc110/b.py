ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,M,X,Y=rl()
x=rl()
y=rl()
x_ = max(x+[X])
y_ = min(y+[Y])

if x_ < y_:
    print('No War')
else:
    print('War')