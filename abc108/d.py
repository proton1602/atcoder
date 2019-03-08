ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

#L=ri()
N_max = 20
M_max = 60

#2^n+3^m+... ([2,n],[3,m],...) List[Tuple[int, int]]
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct 
for L in range(2,101):
    if L<=M_max:
        1
        #print(2,L)
        #for i in range(L):
            #print(1,2,i)
    else:
        fct = factorize(L)
        N = sum(map(lambda x:x[1],fct))
        M = sum(map(lambda x: x[0]*x[1],fct))
        if N<=N_max and M<=M_max:
            1
            #print(N,M)
        else:
            
            print(L, end=' ')
    
