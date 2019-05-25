ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

R,G,B,N=rl()
ans = [0]*(N+1)
ans[0] = 1
for color in [R,G,B]:
    for i in range(N+1):
        temp = i + color
        if temp <= N:
            ans[temp] += ans[i]
print(ans[N])