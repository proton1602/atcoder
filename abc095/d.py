ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,C=rl()
x=[0]*N
x_=[0]*N
v=[0]*N
for i in range(N):
    x[i],v[i] = rl()
    x_[i] = C-x[i]

v_f=[0]*(N+1)
v_b=[0]*(N+1)
for i in range(N):
    v_f[i+1] = v_f[i]+v[i]
    v_b[i+1] = v_b[i]+v[N-i-1]

for i in range(N):
    v_f[i+1] -= x[i]
    v_b[i+1] -= x_[N-i-1]

print(max(max(v_f),max(v_b)))