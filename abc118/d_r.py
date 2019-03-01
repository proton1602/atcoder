N,M = map(int,input().split())
A = list(map(int,input().split()))
c = [2,5,5,4,5,6,3,7,6]

A.sort(reverse=True)

dp = [-1 for _ in range(N+1)]
dp[0] = 0

for a in A:
    c_ = c[a-1]
    for i in range(c_,N+1):
        if dp[i-c_] == -1: continue
        dp[i] = max(dp[i], dp[i-c_]*10 + a)

print(dp[-1])