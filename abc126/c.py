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

N,K=rl()
""" M=[0]*(max(N,K)+2)
k = K
M[k] = 1
while k > 1:
    k = k / 2.0
    ind = int(k//1)
    if k%1 == 0:
        ind -= 1
    M[ind] = 1
for i in range(K,0,-1):
    M[i] += M[i+1]
ans = 0
for i in range(1,N+1):
    ans += (1/2)**(M[i])/N
print(ans)
 """
ans = 0
for i in range(1,N+1):
    ex = 0
    point = i
    while point < K:
        ex += 1
        point *= 2
    ans += (1/2)**ex/N
print(ans)