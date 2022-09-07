import sys
read = sys.stdin.readline

T = int(read())
array = []

for _ in range(T):
    n = int(read())
    array.append(n)

temp_n = int(4*(10e9))
print(temp_n)
a = [False,False]+[True]*(temp_n-1)
primes = []

for i in range(2,temp_n+1):
    if a[i] :
        primes.append(i)
        for j in range(2*i,temp_n+1,i):
            a[j] = False
print(primes)
