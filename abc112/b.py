ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,T=rl()
ans = INF
for _ in range(N):
    c,t = rl()
    if T >= t and ans > c:
        ans = c

print(ans if ans != INF else 'TLE')