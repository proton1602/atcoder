ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))


N,K=rl()
A=rl()

digit = len(format(max(max(A),K),'b'))+1
cnt = [[0,0] for _ in range(digit)]
for i in range(digit):
    for a in A:
        cnt[i][a>>(digit-1-i) & 1] += 1

dp = [[-1,-1] for _ in range(digit)]
dp[0][0]=0

#print(digit)
#print(cnt)


from itertools import product

for i, less in product(range(digit-1),(0,1)):
    if dp[i][less] == -1: continue
    #print('i:{},less:{}'.format(i,less))
    max_d = less or K>>(digit-1-i-1)&1
    #print('max_d',max_d)
    for d in range(max_d+1):
        #print(dp[i][less]*2 + cnt[i+1][1-d])
        dp[i+1][less or d<max_d] = max(dp[i+1][less or d<max_d], dp[i][less]*2 + cnt[i+1][1-d])


print(max(dp[-1]))
