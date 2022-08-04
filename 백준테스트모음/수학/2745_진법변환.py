N,B = input().split()
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sums = 0

for i,n in enumerate(N):
    sums += number.index(n)*(B**(len(N)-i-1))

print(sums)