N,M = map(int,input().split())
cnt = [0]*M
for _ in range(N):
    K,*A = map(int,input().split())
    for a in A:
        cnt[a-1] += 1
print(sum(c==N for c in cnt))