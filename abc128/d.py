import sys
input = sys.stdin.readline
ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7

N,K=rl()
V=rl()
mV = [0]*(N)
mc = 0
for i in range(N):
    v = V[i]
    if v < 0:
        mV[i] = v
        mc += 1
rV = V[::-1]
rmV = mV[::-1]

if K >= (N+mc):
    print(sum(V)-sum(mV))
else:
    ans = 0
    for lc in range(K+1):
        rc = K - lc
        rr = 0
        l_ind = 0
        for ind in range(lc+1):
            if ind > N: break
            rm = lc - ind
            rr_ = sum(V[:ind])-sum(sorted(mV[:ind])[:rm])
            if rr < rr_:
                rr = rr_
                l_ind = ind
        rl = 0
        for ind in range(rc+1):
            if ind + l_ind > N: break
            rm = rc - ind
            rl = max(rl,sum(rV[:ind])-sum(sorted(rmV[:ind])[:rm]))
        ans = max(ans, rr+rl)
    print(ans)

        

