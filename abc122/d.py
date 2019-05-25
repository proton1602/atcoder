ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9 + 7

N=ri()
dp = [[[0 for k in range(4)] for j in range(7)] for i in range(N)]
dp[0][0][0] = 2
dp[0][1][0] = 1
dp[0][5][0] = 1

for i in range(1,N):
    dp[i][0][0] = dp[i-1][0][0]*2 + dp[i-1][2][2] + dp[i-1][3][2] + dp[i-1][4][1]*2 + dp[i-1][5][0]*2 + dp[i-1][5][1] + dp[i-1][6][1]*2 + dp[i-1][6][2]
    dp[i][1][0] = dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][2] + dp[i-1][4][1] + dp[i-1][5][1] + dp[i-1][6][1] 
    dp[i][1][1] = dp[i-1][1][0] + dp[i-1][5][1]
    dp[i][1][2] = dp[i-1][1][1]
    dp[i][2][2] = dp[i-1][1][1]
    dp[i][2][3] = dp[i-1][2][2]
    dp[i][3][2] = dp[i-1][1][1]
    dp[i][3][3] = dp[i-1][3][2]
    dp[i][4][1] = dp[i-1][1][0]
    dp[i][4][2] = dp[i-1][4][1]
    dp[i][5][0] = dp[i-1][0][0] + dp[i-1][2][2] + dp[i-1][3][2] + dp[i-1][5][0] + dp[i-1][6][2]
    dp[i][5][1] = dp[i-1][1][1] + dp[i-1][3][2] + dp[i-1][5][0] + dp[i-1][6][2]
    dp[i][5][2] = dp[i-1][5][1]
    dp[i][6][1] = dp[i-1][1][0]
    dp[i][6][2] = dp[i-1][6][1]
    dp[i][6][3] = dp[i-1][6][2]

ans = dp[N-1][0][0] + dp[N-1][1][0] + dp[N-1][1][1] + dp[N-1][2][2] + dp[N-1][3][2] + dp[N-1][4][1] + dp[N-1][5][0] + dp[N-1][5][1] + dp[N-1][6][1] + dp[N-1][6][2]

print(ans%MOD)