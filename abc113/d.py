ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

H,W,K=rl()
DIV =  1000000007

rc = K-1
dp = [[0 for _ in range(W)] for _ in range(H+1)]
dp[0][0]=1
bar = [1, 1+0, 1+1, 2+1, 3+2, 5+3, 8+5, 13+8, 21+13]

for h in range(1,H+1):
    for w in range(W):
        if w != 0:
            dp[h][w] += dp[h-1][w-1]*bar[w-1]*bar[W-w-1]
        dp[h][w] += dp[h-1][w]*bar[w]*bar[W-w-1]
        if w != W-1:
            dp[h][w] += dp[h-1][w+1]*bar[w]*bar[W-w-2]

print(dp[H][K-1]%DIV)