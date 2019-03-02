ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
INF = 10**18

N=ri()
pri = [0]*101

for i in range(1,N+1):
    b = 2
    while b*b <= i:
        while i%b == 0:
            i //= b
            pri[b] += 1
        b += 1
    if i > 1:
        pri[i] += 1

exp = []
for i in range(101):
    if pri[i] > 0:
        exp += [pri[i] + 1]

exp.sort()
exp_len = len(exp)
import bisect
cnt_75 = exp_len - bisect.bisect_left(exp,75)
cnt_25 = exp_len - bisect.bisect_left(exp,25)
cnt_15 = exp_len - bisect.bisect_left(exp,15)
cnt_5 = exp_len - bisect.bisect_left(exp,5)
cnt_3 = exp_len - bisect.bisect_left(exp,3)
ans = 0

ans += cnt_75
ans += cnt_25*cnt_3 - cnt_25
ans += cnt_15*cnt_5 - cnt_15
ans += cnt_5*(cnt_5-1)/2*cnt_3 - cnt_5*(cnt_5-1)/2*2
ans = int(ans)

print(ans)


