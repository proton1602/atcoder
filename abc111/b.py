ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

ans = [111,222,333,444,555,666,777,888,999]
import bisect
N = ri()
i = bisect.bisect_left(ans,N)
print(ans[i])