ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,M=rl()
ans = [0]*N
for _ in range(M):
    u,v = rl()
    ans[u-1] = v
    ans[v-1] = u

print(*ans, sep=' ')