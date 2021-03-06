ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
INF = 10**18

A,B,Q=rl()
s = [-INF] + rr(A) + [INF]
t = [-INF] + rr(B) + [INF]
X= rr(Q)

import bisect
for x in X:
    s_i = bisect.bisect_left(s,x)
    t_i = bisect.bisect_left(t,x)
    s_l = x-s[s_i-1]
    s_r = s[s_i]-x
    t_l = x-t[t_i-1]
    t_r = t[t_i]-x
    ans = min(
        max(s_l,t_l), s_l+t_r+min(s_l,t_r), s_r+t_l+min(s_r,t_l), max(s_r,t_r)
    )
    print(ans)