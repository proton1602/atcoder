ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

x=ri()
#YN(x==3 or x==5 or x==7)
#YN([3,5,7].count(x))
YN(x in (3,5,7))