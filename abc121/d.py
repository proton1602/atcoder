ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

A,B=rl()
A -= 1

a2 = format(A,'b')
al = len(a2)
b2 = format(B,'b')
bl = len(b2)


bc = [0]*bl
bc[0] += (B+1)//2
bc[0] -= (A+1)//2
for i in range(1,bl):
    bc[i] += (B+1)//(2**(i+1))*(2**i) + max(0, (B%(2**(i+1)) - (2**i-1)))
    bc[i] -= (A+1)//(2**(i+1))*(2**i) + max(0, (A%(2**(i+1)) - (2**i-1)))

ans = 0
for i in range(bl):
    if bc[i]%2==1:
        ans += 2**i

print(ans)