N = int(input())
#A = [int(i) for i in input().split()]
A = list(map(int,input().split()))

def gcp(a,b):
    if b == 0:
        return a
    else:
        return gcp(b,a%b)

a = A[0]
for i in range(1,N):
    a = gcp(a,A[i])
print(a)