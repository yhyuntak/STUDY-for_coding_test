



#220926
# 힙큐라는것에 대해 알아봐야겠군.
import heapq

N = int(input())
array = []
for _ in range(N):
    heapq.heappush(array,int(input()))

save = 0
for i in range(1,N):
    sums = heapq.heappop(array)+heapq.heappop(array)
    heapq.heappush(array,sums)
    save+=sums

print(save)
