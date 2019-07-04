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

N,M=rl()
S1 = [set() for _ in range(N+1)]
S2 = [set() for _ in range(N+1)]
S3 = [set() for _ in range(N+1)]
for i in range(M):
    u,v=rl()
    S1[u].add(v)
S,T=rl()

for i in range(1,N+1):
    S_ = S1[i]
    if len(S_) != 0:
        for s in S_:
            S2[i] = S2[i] | S1[s]
for i in range(1,N+1):
    S_ = S2[i]
    if len(S_) != 0:
        for s in S_:
            S3[i] = S3[i] | S1[s]

ans = -1
R = [INF for _ in range(N+1)]
R[S] = 0
import heapq
Se = []
heapq.heappush(Se,(0,S))
Sel = 1
L = set()
while Sel>0:
    node_m, node = heapq.heappop(Se)
    Sel -= 1
    for node_s in S3[node]:
        if node_m+1 < R[node_s]:
            R[node_s] = node_m + 1
            heapq.heappush(Se,(node_m+1,node_s))
            Sel += 1

if R[T] != INF:
    ans = R[T]

print(ans)
