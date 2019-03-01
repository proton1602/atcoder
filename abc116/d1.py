ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,K=rl()

td_1 = [0]*N
td_rem = []
for _ in range(N):
    t,d = rl()
    t -= 1
    if td_1[t] == 0:
        td_1[t] = d
    else:
        if d <= td_1[t]:
            td_rem += [d]
        else:
            td_rem += [td_1[t]]
            td_1[t] = d


td_1.sort(reverse=True)
td_rem.sort(reverse=True)
#print(td_1)
#print(td_rem)
import numpy as np
index_0 = td_1.index(0) if 0 in td_1 else len(td_1)
td_1 = list(np.cumsum([0] + td_1[:index_0]))
td_rem = list(np.cumsum([0]+td_rem))

ans = [0 for _ in range(K+1)]
sum_l = 0
for i in range(1,K+1):
    if len(td_1)-1 >= i and len(td_rem)-1>=K-i:
        ans[i] = i*i + td_1[i] + td_rem[K-i]

#print(td_1)
#print(td_rem)
#print(ans)
print(max(ans))
