ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

A,B,Q=rl()
s=[0]*(A+2)
t=[0]*(B+2)
X=[0]*Q
for i in range(1,A+1):
    s[i]=ri()
s[0],s[A+1]=-float('inf'),float('inf')

for i in range(1,B+1):
    t[i]=ri()
t[0],t[B+1]=-float('inf'),float('inf')

for i in range(Q):
    X[i]=ri()

import bisect
for x in X:
    s_i = bisect.bisect_left(s,x)
    t_i = bisect.bisect_left(t,x)
    s_l = x-s[s_i-1]
    s_r = s[s_i]-x
    t_l = x-t[t_i-1]
    t_r = t[t_i]-x
    ans = min(
        [max(s_l,t_l), s_l+t_r+min(s_l,t_r), s_r+t_l+min(s_r,t_l), max(s_r,t_r)]
    )
    print(ans)