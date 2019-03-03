ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N=ri()
T,A=rl()
H=rl()
dif = INF
ans = 0
for i in range(N):
    res = abs(A - (T-H[i]*0.006))
    if dif > res:
        dif = res
        ans = i+1

print(ans)