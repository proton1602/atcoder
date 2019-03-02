ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
INF = 10**18

N=ri()
dig = len(str(N))
ans = 0
if N>=357:
    for d in range(3,dig):
        ans += 3**d - 3*(2**d) + 3
    import itertools
    item = [3,5,7]
    for dl in itertools.product(item,repeat=dig):
        if 3 not in dl or 5 not in dl or 7 not in dl:
            continue
        n = 0
        for i in range(dig):
            n += dl[i]*(10**i)
        if N >= n:
            ans += 1

print(ans)

