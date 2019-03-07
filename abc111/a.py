ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

n=input()
ans = ''
for s in n:
    if s=='1':
        ans += '9'
    elif s=='9':
        ans += '1'
    else:
        ans += s

print(int(ans))