ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD=10**9+7

r,D,x=rl()
for i in range(10):
    x = r*x-D
    print(x)