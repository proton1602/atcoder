A,B,C,X,Y=list(map(int,input().split()))
print(min([i*2*C+max(0,X-i)*A+max(0,Y-i)*B for i in range(10**5+1)]))
