N,M = map(int,input().split())
_, *A = map(int,input().split())
s = set(A)
for i in range(N-1):
    _, *B = map(int,input().split())
    s &= set(B)
print(len(s))