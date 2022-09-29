import sys
read = sys.stdin.readline

n = int(read())

for _ in range(n):
    a,b = map(int,read().split())
    aa,bb = a,b

    while a % b != 0 :
        a,b = b, a%b

    print(aa*bb//b)
