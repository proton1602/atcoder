ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,M=rl()
A = [0]*M
B = [0]*M
ad = {i:[] for i in range(1,N+1)}
for i in range(M):
    a,b=rl()
    A[i],B[i]=a,b
    ad[a].append(b)
    ad[b].append(a)

print(ad)

def connect_check(ad,a,b):
    if ad[a] == [] or ad[b] == []:
        return False
    elif b in ad[a]:
        return True
    else:
        for c in ad[a]:
            res = connect_check(ad,c,b)
            if res:
                return True
        return False

def con_list(ad,a,b):
    a_l = {a}
    b_l = {b}
    
    while True:
        


for a,b in zip(A,B):
    ad[a].remove(b)
    ad[b].remove(a)
    