ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,Q=rl()
S=input()
L,R=[0]*Q,[0]*Q
for i in range(Q):
    L[i],R[i] = rl()
s = [0]*(N+2)
ss = [0]*(N+2)
for i in range(N-1):
    if S[i] == 'A' and S[i+1] == 'C':
        s[i] = 1
        s[i+1] = 1

ss[0] = s[0]
for i in range(1,N):
    ss[i] = ss[i-1] + s[i]

for i in range(Q):
    l,r = L[i],R[i]
    l -= 1
    r -= 1
    res = (ss[r] - ss[l-1])//2
    if s[r]==1 and s[l]==1 and S[r]=='A' and S[l]=='C':
        res -= 1
    print(res)