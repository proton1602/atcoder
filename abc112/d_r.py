ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,M=rl()

if M%N==0:
    print(M//N)
else:
    x = M//N
    ans = 1
    l=[]
    for i in range(1,int(M**0.5)+1):
        if M%i==0:
            l.append(i)
            l.append(M//i)
    l.sort()

    import bisect
    l_i = bisect.bisect_right(l,x)-1
    print(l[l_i])