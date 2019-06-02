ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
S=input()
white = [0] * (N+1)
black = [0] * (N+1)
for i in range(N):
    if S[N-1-i] == '.':
        white[i] = white[i-1] + 1
    else:
        white[i] = white[i-1]
    if S[i] == '#':
        black[i] = black[i-1] + 1
    else:
        black[i] = black[i-1]
ans = black[-1] + white[N-1]
for i in range(N):
    ans = min(ans, black[i] + white[N-2-i])
print(ans)