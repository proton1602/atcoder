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
coler = [0]*N
ME = [None]*N
MO = [None]*N
UVW=[]
for i in range(N-1):
    u,v,w = rl()
    u -= 1
    v -= 1
    if w%2 == 1:
        if MO[u] == None:
            MO[u] = [v]
        else:
            MO[u].append(v)
        if MO[v] == None:
            MO[v] = [u]
        else:
            MO[v].append(u)
    else:
        if ME[u] == None:
            ME[u] = [v]
        else:
            ME[u].append(v)
        if ME[v] == None:
            ME[v] = [u]
        else:
            ME[v].append(u)

from collections import deque
q = deque([0])
visited = [False]*N
while len(q)>0:
    n = q.popleft()
    if visited[n] == True:
        continue
    else:
        visited[n] = True
    v = coler[n]
    e = ME[n]
    if not e is None:
        q.extend(e)
        for en in e:
            coler[en] = v
    o = MO[n]
    if not o is None:
        v += 1
        q.extend(o)
        for on in o:
            coler[on] = v

for c in coler:
    print(c%2)
    

