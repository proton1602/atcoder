ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

n=ri()
a=rl()
a.sort()


import bisect

p = a[-1]
p2 = p/2
q_i = bisect.bisect_left(a,p2)
if ((a[q_i]-p2) > (p2 - a[q_i-1]) or p==a[q_i]) and q_i != 0:
    q_i -= 1
q = a[q_i]

print(p,q)