ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,M,C=rl()
B=rl()
ans = 0
for _ in range(N):
    A=rl()
    if sum(map(lambda x,y:x*y,A,B))+C > 0:
        ans += 1
    
print(ans)