ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,K=rl()
td = [rl() for _ in range(N)]

td_n = {}
for t,d in td:
    if t in td_n:
        td_n[t] += [d]
    else:
        td_n[t] = [d]
td = []
n = len(td_n)
for t,d in td_n.items():
    d.sort(reverse=True)
    td += [d]

#print(td)
td_len = [len(t) for t in td]
td_len.sort(reverse=True)
td_1 = [t[0] for t in td]
td_1.sort(reverse=True)
td_rem = [d for t in td for d in t[1:]]
td_rem.sort(reverse=True)

ans = [0 for _ in range(n+1)]
sum_l = 0
for i in range(1,n+1):
    sum_l += td_len[i-1]
    if sum_l < K:
        continue
    else:
        ans[i] = i*i + sum(td_1[:i]) + sum(td_rem[:(K-i)])

print(td_1)
print(td_rem)
print(ans)
print(max(ans))
