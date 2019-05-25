ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

A=rr(5)
x = 10
for a in A:
    x = min(x,a%10 if a%10 !=0 else 10)

s = 0
for a in A:
    s += (a//10)*10
    s += 10 if a%10 != 0 else 0

print(s-10+x)