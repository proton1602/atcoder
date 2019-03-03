ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

n = ri()
if n==1:
    print('Hello World')
else:
    A=ri()
    B=ri()
    print(A+B)