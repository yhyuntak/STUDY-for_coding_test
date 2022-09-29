import heapq

N = int(input())

heap = []

array = []
for _ in range(N):
    heapq.heappush(heap,int(input()))

save = 0
for i in range(1,len(heap)):
    temp = heapq.heappop(heap)+heapq.heappop(heap)
    save += temp
    heapq.heappush(heap,temp)

print(save)