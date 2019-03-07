ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,K=rl()
a,b=0,0
ans=0
if K==0:
    ans = N*N
else:
    for b in range(K+1,N+1):
        n = N%b
        ans += b-K
        if n < K:
            ans +=(N//b-1)*(b-K)
        elif K<=n and n<b:
            ans += N//b*(b-K) - (b-n-1)


print(ans)
        