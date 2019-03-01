#H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
#print(A)
A_flt = []
for s in A:
    A_flt.extend(s)
#print(A_flt)
import collections
A_cnt = collections.Counter(A_flt)
#print(A_cnt)
if A_cnt.most_common()[0][1] >= 3:
    print('NO')
else:
    print('YES')
