N,M=map(int,input().split())
X=list(map(int,input().split()))

X.sort()
#print(X)
d = [X[i]-X[i-1] for i in range(1,M)]
d.sort()
#print(d)
#print(sum(d[:-(N-1)]) if M-N>0 else 0)
print(sum(d[0:(M-N)]) if (M-N)>0 else 0)