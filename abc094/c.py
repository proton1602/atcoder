ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
X=rl()
Xs = sorted(X)
Xsl = Xs[:N//2]
Xsr = Xs[N//2:]
r = Xsr[0]
l = Xsl[-1]

for x in X:
    if x <= l:
            print(r)
    else:
            print(l)

