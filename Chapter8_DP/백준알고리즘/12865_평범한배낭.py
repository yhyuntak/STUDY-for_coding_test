import sys
read = sys.stdin.readline

N,K = map(int,read().split())
bags = [[]]
for _ in range(N):
    bags.append(list(map(int,read().split())))

# knapsack에 패딩 넣어주기
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for y in range(1,N+1):
    # 현재 물건 저장하기
    now_stuff = bags[y]
    weight = now_stuff[0]
    value = now_stuff[1]
    for x in range(1,K+1):
        # 현재 물건의 무게(weight)가 현재 가방의 제한 무게(x)보다 크면
        # 현재 물건은 넣을수 없으니 이전 물건의 값(y-1,x)을 받아오기
        if x < weight :
            knapsack[y][x] = knapsack[y-1][x]
        # 그게 아니라면 현재 물건을 넣을 수 있으니,
        # 현재 물건의 value와 와 이전 물건에서 남은 가방의 무게만큼의 넣을 수 있는 최대 value의 합과
        # 이전 물건까지의 value를 비교해서 더 큰 값을 저장한다.
        else :
            knapsack[y][x] = max( value + knapsack[y-1][x-weight] , knapsack[y-1][x])

# knapsack의 제일 마지막 column의 제일 마지막 row값을 출력하자.
print(knapsack[-1][-1])