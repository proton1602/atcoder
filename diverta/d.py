ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
ans = 0
for i in range(1,int(N**(1/2))+1):
    if (N-i)%i==0:
        temp = (N-i)//i
        if temp > i:
            ans += temp
print(ans)