ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
U=[0]*N #u = x + y
V=[0]*N #v = x - y
parity = 0
for i in range(N):
    x,y = rl()
    U[i],V[i] = format(x+y,'+032b'), format(x-y,'+032b')
    parity += (x+y)%2

if parity == 0 or parity == N:
    parity //= N
    m = 31 if parity else 32
    print(m)
    d = [1 for i in range(m)]
    for i in range(1,31):
        d[i] = d[i-1]*2
    d.sort(reverse=True)
    print(*d, sep=' ')

    for i in range(N):
        res = ''
        u,v = U[i],V[i]

        ub,vb = [1]+list(map(int,u[1:-1])), [1]+list(map(int,v[1:-1]))
        if not parity:
            ub += [0]
            vb += [0] 
        if u[0] == '-': ub = list(map(lambda x: x^1, ub))
        if v[0] == '-': vb = list(map(lambda x: x^1, vb))

        for ub_,vb_ in zip(ub,vb):
            if ub_==0 and vb_==0:
                res += 'L'
            elif ub_==1 and vb_==1:
                res += 'R'
            elif ub_==0 and vb_==1:
                res += 'D'
            else:
                res += 'U'
        print(res)
else:
    print(-1)
