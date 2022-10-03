"""
점화식은

d[n] = max(d[n-2] , d[n-3]+g[n-1]) 이다.
d[n-2]는 해당 칸의 2번째 전의 계단을 밟고 2계단 뛴거로 보고
d[n-3]+g[n-1]은 1계단만 오를건데 연속을 피하기 위해서, d[n-3]을 보는 것.
"""

N = int(input())
array = [0]
for _ in range(N):
    array.append(int(input()))
d = [0 for _ in range(N+1)]

if N == 1 :
    d[1] = array[1]
    print(d[1])
elif N == 2 :
    d[2] = array[1]+array[2]
    print(d[2])
else :
    d[1] = array[1]
    d[2] = array[1]+array[2]
    for n in range(3,N+1):
        d[n] = max(d[n-2],d[n-3]+array[n-1]) + array[n]
    print(d[-1])