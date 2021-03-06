N,M=map(int,input().split())
A = list(map(int,input().split()))

c = [2,5,5,4,5,6,3,7,6]

dp = [[-1 for n in range(N+1)] for m in range(M+1)]
dp[0][0] = 0
#keta
dp_r = [[-1 for n in range(N+1)] for m in range(M+1)]
#m

d = {}
for a in A:
    d[a] = c[a-1]
#print(d)

inv_d = {}
for k,v in d.items():
    if v in inv_d:
        if k > inv_d[v]:
            inv_d[v] = k
    else:
        inv_d[v] = k
#print(inv_d)

s_A = sorted(inv_d.items(), key=lambda x:x[0],reverse=True)
#print(s_A)
A = [a[1] for a in s_A]
M = len(A)

for m in range(1,M+1):
    for n in range(N+1):
        #dp[m][n] = max(dp[m-1][n],
        #dp[m][n-c[A[m-1]-1]] + 1 if (n-c[A[m-1]-1])>=0 and dp[m][n-c[A[m-1]-1]] != -1 else -1)
        if n-c[A[m-1]-1] >= 0 and dp[m][n-c[A[m-1]-1]] != -1:
            if dp[m-1][n] < (dp[m][n-c[A[m-1]-1]] + 1):
                dp[m][n] = dp[m][n-c[A[m-1]-1]] + 1
                dp_r[m][n] = 1
            elif dp[m-1][n] == (dp[m][n-c[A[m-1]-1]] + 1):
                dp[m][n] = dp[m][n-c[A[m-1]-1]] + 1
                dp_r[m][n] = 2
            else:
                dp[m][n] = dp[m-1][n]
                dp_r[m][n] = 0
        else:
            dp[m][n] = dp[m-1][n]
            dp_r[m][n] = 0


#import pprint
#pprint.pprint(dp,width=100)
#pprint.pprint(dp_r,width=100)

def trace(dp,m,n):
    r=[[]]
    for _ in range(N+M+2):
        if m==0 and n==0:
            return r
        elif dp_r[m][n] == 0:
            m = m-1
        elif dp_r[m][n] == 1:
            r = [r_+[m] for r_ in r]
            n = n-c[A[m-1]-1]
        elif dp_r[m][n] == 2:
            r_1 = trace(dp,m-1,n)
            r_2 = trace(dp,m,n-c[A[m-1]-1])
            return [r[0]+r_ for r_ in r_1] + [r[0]+r_+[m] for r_ in r_2]

tm = trace(dp,M,N)

ans = []
for tm_ in tm:
    ans_ = [inv_d[c[A[m-1]-1]] for m in tm_]
    ans_.sort(reverse=True)
    ans += [ans_]

ans.sort(reverse=True)
#print(ans)
for ans_ in ans[0]:
    print(ans_,sep='',end='')
print()