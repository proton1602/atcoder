import numpy as np
import collections
L = int(input())
A = [int(input()) for _ in range(L)]
print(L)
print(A)
A_2 = np.array(list(map(lambda x: x%2, A)))
A_odd_index = np.where(A_2 == 1)[0]
print(A_odd_index)
A_odd_ren = A_odd_index - np.array(range(len(A_odd_index)))
A_odd_ren_cnt = collections.Counter(A_odd_ren)
print(A_odd_ren_cnt)
A_odd_ren_cnt_des = A_odd_ren_cnt.most_common()
print(A_odd_ren_cnt_des)
print(type(A_odd_ren_cnt_des[0][1]))
odd_cont = np.array([])
index_max = 0
for i in range(len(A_odd_ren_cnt_des)):
    print(i)
    if index_max <= A_odd_ren_cnt_des[i][1]:
        print("index")
        index_max = A_odd_ren_cnt_des[i][1]
        odd_cont = np.append(odd_cont,A_odd_ren_cnt_des[i][0])
    else:
        break
odd_cont = odd_cont.astype('int')
print(odd_cont.astype('int'))
s_index = []
for i in range(len(odd_cont)):
    print(np.where(A_odd_ren == odd_cont[i]))
    s_index.append([np.where(A_odd_ren == odd_cont[i])[0], 
        np.where(A_odd_ren == odd_cont[i])[-1] + 1])
print(s_index)

