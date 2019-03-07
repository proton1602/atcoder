ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

n = ri()
v=rl()
a = []
b = []
for i in range(0,n,2):
    a.append(v[i])
for i in range(1,n,2):
    b.append(v[i])

import collections
ca = collections.Counter(a)
ca = ca.most_common()
cb = collections.Counter(b)
cb = cb.most_common()
la = len(a)
lb = len(b)

if ca[0][0] != cb[0][0]:
    ans = (la - ca[0][1]) + (lb - cb[0][1])
else:
    ans = []
    if len(ca) >= 2:
        ans.append(la-ca[1][1] + lb-cb[0][1])
    if len(cb) >= 2:
        ans.append(la-ca[0][1] + lb-cb[1][1])
    if len(ca)==1 and len(cb)==1:
        ans.append(ca[0][1])
        ans.append(cb[0][1])
    ans = min(ans)

print(ans)