#最大公約数
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

#最大公約数_list
def gcd_list(L):
    v = L[0]
    for i in range(1, len(L)):
        v = gcd(v, L[i])
    return v

#最小公約数
def lcm(a,b):
    return a*b//gcd(a,b)

#最小公約数_list
def lcm_list(L):
    v = L[0]
    for i in range(1,len(L)):
        v = lcm(v,L[i])
    return v
