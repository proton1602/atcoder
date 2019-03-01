def main():
    input()
    A = list(map(int,input().split()))

    b = min(A)
    for a in A:
        while True:
            if a%b == 0:
                break
            a,b = b, a%b
    print(b)

main()