import sys

read = sys.stdin.readline

K,N = map(int,read().split())
array = []
for _ in range(K):
    array.append(int(read()))

start = 1
end = max(array)

while start<=end :
    mid = (start+end)//2
    temp = 0
    for a in array:
        temp += (a//mid)

    if temp >= N :
        start = mid+1
    else :
        end = mid-1

print(end)

