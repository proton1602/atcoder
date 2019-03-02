ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
INF = 10**18

S=input()

ans = INF
for i in range(len(S)-2):
    rst = abs(753 - int(S[i:i+3]))
    if ans > rst:
        ans = rst

print(ans)