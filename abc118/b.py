N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

A = [flatten for inner in A for flatten in inner[1:]]
#print(A)
import collections
A_cnt = collections.Counter(A)
print(sum([l[1]==N for l in A_cnt.most_common()]))
