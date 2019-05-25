ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

A=input()
B=input()
S=input()
Al=len(A)
Bl=len(B)
Sl=len(S)

a_o = ord('a')
As = [[0]*26]
As_ = [0]*26
Bs = [[0]*26]
Bs_ = [0]*26
Ss = [[0]*26]
Ss_ = [0]*26
for a in A[::-1]:
    As_[ord(a)-a_o] += 1
    As.append(As_.copy())
As = As[::-1]
for b in B[::-1]:
    Bs_[ord(b)-a_o] += 1
    Bs.append(Bs_.copy())
Bs = Bs[::-1]
for s in S[::-1]:
    Ss_[ord(s)-a_o] += 1
    Ss.append(Ss_.copy())
Ss = Ss[::-1]

def dfs(i,j,k):
    if i==Sl or (j==Al and k==Bl):
        return 0
    res = []
    for l in range(26):
        if Ss[i][l] == 0: continue
        As_ = As[j][l] if j!=Al else 0
        Bs_ = Bs[k][l] if k!=Bl else 0
        if As_+Bs_<Ss[i][l]:
            return Al+Bl
    if j != Al and As[j][ord(S[i])-a_o] >= 0:
        for j_ in range(j,Al):
            if A[j_] == S[i]:
                res.append(j_ - j + 1 + dfs(i+1,j_+1,k))
                break
    if k != Bl and Bs[k][ord(S[i])-a_o] >= 0:
        for k_ in range(k,Bl):
            if B[k_] == S[i]:
                res.append(k_ - k + 1 + dfs(i+1,j,k_+1))
                break
    return min(res)

def bfs(i,j,k):
    if i==Sl or (j==Al and k==Bl):
        return i+j
    for l in range(26):
        if Ss[i][l] == 0: continue
        As_ = As[j][l] if j!=Al else 0
        Bs_ = Bs[k][l] if k!=Bl else 0
        if As_+Bs_<Ss[i][l]:
            return Al+Bl
    queue = []
    queue.append([i,j,k,0])
    queue.append([i,j,k,1])
    while len(queue)>0:
        i,j,k,pol=queue.pop(0)
        if i==Sl or (j==Al and k==Bl):
            res = j+k
            for i,j,k,pol in queue:
                res = min(res,j+k)
            return res
        if pol==0:
            if j != Al and As[j][ord(S[i])-a_o] >= 0:
                for j_ in range(j,Al):
                    if A[j_] == S[i]:
                        cont = 1
                        for l in range(26):
                            if Ss[i][l] == 0: continue
                            As_ = As[j][l] if j!=Al else 0
                            Bs_ = Bs[k][l] if k!=Bl else 0
                            if As_+Bs_<Ss[i][l]:
                                cont = 0
                                break
                        if cont:    
                            queue.append([i+1,j_+1,k,0])
                            queue.append([i+1,j_+1,k,1])
                        break
        else:
            if k != Bl and Bs[k][ord(S[i])-a_o] >= 0:
                for k_ in range(k,Bl):
                    if B[k_] == S[i]:
                        cont = 1
                        for l in range(26):
                            if Ss[i][l] == 0: continue
                            As_ = As[j][l] if j!=Al else 0
                            Bs_ = Bs[k][l] if k!=Bl else 0
                            if As_+Bs_<Ss[i][l]:
                                cont = 0
                                break
                        if cont:    
                            queue.append([i+1,j,k_+1,0])
                            queue.append([i+1,j,k_+1,1])
                        break

i,j,k,ans=[0,0,0,0]
ABp = []
res = []
for l in range(26):
    if Ss[i][l] == As[j][l]+Bs[k][l]:
        ABp.append(l)
if len(ABp) != 0:
    for i_ in range(Sl-1,-1,-1):
        if ord(S[i_])-a_o in ABp:
            i = i_+1
            break
    for j_ in range(Al-1,-1,-1):
        if ord(A[j_])-a_o in ABp:
            j = j_+1
            break
    for k_ in range(Bl-1,-1,-1):
        if ord(B[k_])-a_o in ABp:
            k = k_+1
            break
    for j_ in range(j,Al):
        if all([As[0][l]-As[j_][l]+Bs[0][l]-Bs[k][l]==Ss[0][l]-Ss[i][l] for l in range(26)]):
            res.append(bfs(i,j_,k))
            break
    for k_ in range(k,Bl):
        if all([As[0][l]-As[j][l]+Bs[0][l]-Bs[k_][l]==Ss[0][l]-Ss[i][l] for l in range(26)]):
            res.append(bfs(i,j,k_))
            break

if len(res)!=0:
    print(min(res))
else:
    print(bfs(i,j,k))

