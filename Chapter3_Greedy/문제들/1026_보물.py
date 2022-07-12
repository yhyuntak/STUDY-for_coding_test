import sys
read = sys.stdin.readline

N = int(read())
A = list(map(int,read().split()))
B = list(map(int,read().split()))

# A는 오름차순
A.sort()
# B는 내림차순
B.sort(reverse=True)

summation = 0
for i in range(N):
    summation += A[i]*B[i]

print(summation)