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

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

N=ri()
A=list(rl())
L=[0]*(N+2)
R=[0]*(N+2)
L[0] = A[0]
R[N-1] = A[N-1]
for i in range(1,N):
    L[i] = gcd(L[i-1],A[i])
for i in range(N-2,-1,-1):
    R[i] = gcd(R[i+1],A[i])

ans = 0
for i in range(N):
    ans = max(ans,gcd(L[i-1],R[i+1]))
print(ans)