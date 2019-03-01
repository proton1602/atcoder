N,M = map(int,input().split())
A = list(map(int,input().split()))
c=[2,5,5,4,5,6,3,7,6]

dp = [-1 for _ in range(N+1)]
dp[0] = 0

for i in range(N+1):
    for a in A:
        if i-c[a-1]>=0:
            dp[i] = max(dp[i], dp[i-c[a-1]]*10 + a)

print(dp[-1])
