ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

A,B,K=rl()
for i in range(100,0,-1):
    if A%i == 0 and B%i==0:
        K -= 1
    if K==0:
        print(i)
        break