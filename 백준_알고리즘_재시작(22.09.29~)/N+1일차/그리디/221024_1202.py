"""

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다.
상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

"""

from collections import deque()

N,K = map(int,input().split())
jews = []
bags = deque()
for _ in range(N):
    jews.append(list(map(int,input().split())))
for _ in range(K):
    bags.append(int(input()))

# 보석과 가방의 수가 많다.
# 가치가 높은 보석들로 내림차순 정렬하면서 무게도 내림차순 정렬해서
jews.sort(key=lambda x:-x[0])
bags.sort()
for _ in range(K):
    now_bag = bags.popleft()
    for i in range(len(jews)):
        
