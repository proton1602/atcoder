import sys
input = sys.stdin.readline
ri = lambda: int(input())
#rl = lambda: [int(x) if x.isdecimal() else x for x in input().split()]
#rl = lambda: list(input().split()))
rl = lambda: map(int,input().split())
rr = lambda N: [list(l) for l in zip(*[rl() for _ in range(N)])]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7

N = ri()
XY = []
for i in range(N):
    x,y=rl()
    XY.append((x,y))
XY.sort()
XYD = []
for i in range(N):
    x,y = XY[i]
    ret = []
    for j in range(i+1,N):
        ret.append((XY[j][0] - x, XY[j][1] - y))
    XYD.extend(ret)

import collections
c = collections.Counter(XYD).most_common()
if N == 1:
    print(1)
else:
    print(N-c[0][1])
