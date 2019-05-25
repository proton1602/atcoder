ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9 + 7

N,X=rl()
S=rl()
S.sort()

import bisect
cnt_0 = bisect.bisect_right(S,X)

def search(s,n,x):
    print(s,n,x)
    if n==1:
        return x%S[0]
    ret = 0
    for i in range(n):
        res = 0
        x_ = x%s[i]
        ind = bisect.bisect_right(S,x_)
        if ind == 0:
            res = x_
        else:
            res = search(S[:ind],ind,x_)
        for j in range(n-ind,n+1):
            res = res*j%MOD
        ret = (ret + res)%MOD
    return ret

res = search(S[:cnt_0],cnt_0,X)
for j in range(N-cnt_0,N+1):
    res = res*j%MOD
print(res)