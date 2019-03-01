ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N=ri()
A=rl()

d = [0]*(N+1)
d[0] = A[0]
sum = abs(A[0])
for i in range(1,N):
    dif = A[i]-A[i-1]
    d[i] = dif
    sum += abs(dif)
d[N]= 0-A[N-1]
sum += abs(A[N-1])


for i in range(1,N+1):
    if d[i-1]*d[i] >= 0:
        print(sum)
    else:
        print(sum-2*min(abs(d[i-1]),abs(d[i])))
