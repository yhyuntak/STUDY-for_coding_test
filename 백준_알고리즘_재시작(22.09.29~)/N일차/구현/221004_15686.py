import sys
read = sys.stdin.readline

N,M = map(int,input().split())
# 집 리스트와 치킨집 리스트들을 따로 뽑아놓자.
house_list = []
chicken_list = []

for r in range(N):
    temp = list(map(int,read().split()))
    for c,t in enumerate(temp) :
        if t == 1 : # house
            house_list.append([r,c])
        elif t == 2 :
            chicken_list.append([r,c])

"""
일단 치킨집들의 조합을 찾자.
"""
from itertools import permutations,combinations
comb_chicken = list(combinations(chicken_list,M))


"""
치킨집 루프 :
    하우스 루프 : 거리를 구해서 도시의 치킨 거리를 매번 구하자.
이게 bfs보다 더 효율적임.
"""
final_min_dist = 10e9
for chickens in comb_chicken : # 한 세트씩 꺼내기
    # 한 치킨집들의 세트당 모든 집들의 최소 치킨 거리를 구해서 each min dist에 저장한다.
    each_min_dist = []
    for house in house_list :
        min_dist = 10e9
        for chicken in chickens :
            min_dist = min(min_dist,abs(chicken[0]-house[0])+abs(chicken[1]-house[1]))
        each_min_dist.append(min_dist)
    # 저장된 each min dist와 지금까지의 도시의 치킨거리와 비교해서 최소값을 가진다.
    final_min_dist = min(final_min_dist,sum(each_min_dist))
print(final_min_dist)