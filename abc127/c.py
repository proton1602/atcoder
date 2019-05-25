ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD=10**9+7

N,M=rl()
L=[0]*M
R=[0]*M
for i in range(M):
    L[i],R[i] = rl()

gate = [0]*(N+2)
for l,r in zip(L,R):
    gate[l] += 1
    gate[r+1] -= 1
for i in range(1,N+1):
    gate[i] += gate[i-1]

print(gate.count(M))