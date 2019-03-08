#�ő���� O(log(max(a,b)))
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

#�ő����_list O(Nlog(max(L)))
def gcd_list(L):
    v = L[0]
    for i in range(1, len(L)):
        v = gcd(v, L[i])
    return v

#�ŏ�����
def lcm(a,b):
    return a*b//gcd(a,b)

#�ŏ�����_list
def lcm_list(L):
    v = L[0]
    for i in range(1,len(L)):
        v = lcm(v,L[i])
    return v
