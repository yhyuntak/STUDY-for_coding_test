n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort() # 10 15 17 19

start = 0
end = array[-1]
mid = (start+end)//2

while (start<=end) :
    total = 0
    mid = (start+end)//2
    for x in array:
        if x-mid > 0 :
            total += (x-mid)
    if total == m:
        break
    elif total > m : # 떡 양이 많다면 -> 오른쪽을 탐색하라.
        start = mid +1
    elif total < m : #떡 양이 부족하다 -> 왼쪽을 탐색하라.
        end = mid - 1

# 19 15 10 17

print(mid)
