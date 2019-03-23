ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
b=rl()

def ANS():
    ans = []
    for i in range(N):
        rm_i = -1
        for j in range(N-i):
            if b[j] == (j+1):
                rm_i = j
            if j==(N-i-1) and rm_i==-1:
                return -1
        ans.append(b.pop(rm_i))
    return ans
    
res = ANS()
if res==-1:
    print('-1')
else:
    for r in res[::-1]:
        print(r)
