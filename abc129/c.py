MOD = 10**9+7

N,M=map(int,input().split())
A=[0]*M
for i in range(M):
    A[i] = int(input())

dp = [0]*(N+4)
dp[0] = 1
for a in A:
    dp[a] = -1

for i in range(1,N+1):
    if dp[i] != -1:
        if dp[i-2] != -1:
            dp[i] += dp[i-2]
        if dp[i-1] != -1:
            dp[i] += dp[i-1]
        dp[i] = dp[i] % MOD

print(dp)