A,B=list(map(int,input().split()))

ans = 0
for i in range(A,B+1):
    s = str(i)
    if s[0]==s[4] and s[1]==s[3]:
        ans+=1

print(ans)