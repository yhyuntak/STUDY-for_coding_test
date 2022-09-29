"""
NXM 크기의 판, 각 판에는 최대 적이 하나씩
N+1 번행의 모든 칸에는 성이 있다.

성에 궁수를 3명 배치할 것. 하나에 최대 1명
모든 궁수가 동시에 공격하되 각각 하나씩만 공격가능
궁수가 공격하는 적은 거리가 d 이하인 적 중 가장 가까운 적
여럿일 경우엔 가장 왼쪽에 있는 적을 공격, 같은 적을 여러 궁수가 공격할 수 있다

공격받은 적은 제외된다.

공격이 끝나면 적은 한칸 아래로 이동하고 성이 있는 칸으로 이동되면 게임에서 제외

모든 적이 없어지면 게임 끝

궁수가 최대로 제거가능한 적은?

참고로 거리는 대각선으로 잴 수 없다. 한칸 한칸이 거리임.


"""

from itertools import combinations
from copy import deepcopy

N,M,D = map(int,input().split())
graph = []
for _ in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)

# 모든 궁수의 케이스에 대해 확인하고 MAX 값을 찾아야한다.
archers = [i for i in range(M)]
max_remove = 0

for archer_case in list(combinations(archers,3)) :
    # 각 궁수의 케이스에서 N번 씩 진행이 되어야함.
    # N번이 끝나면 어떻게 되었든 모든 적이 0가 되기 때문이다.
    case_remove = 0
    find_enermy = []
    temp_graph = deepcopy(graph)
    for n in range(N):
        # 구현할 것은 각 궁수마다 거리 D안에 있는 적 중 가장 가까운 것들을
        # 찾으면서, 가장 왼쪽에 있는 놈을 노리면 된다.
        for archer in archer_case:
            # 일단 각 궁수마다 D 거리 안에 적이 있는지 파악부터 할까
            # 그래프를 다 훑는게 나을지도.
            temp_enermy = []
            for r in range(N):
                for c in range(M):
                    distance = abs(r-N)+abs(c-archer)
                    if distance <= D and temp_graph[r][c] == 1:
                        temp_enermy.append([distance,r,c])
            # 거리순 정렬하고, column순 정렬하기(제일왼쪽)
            temp_enermy.sort(key=lambda x:(x[0],x[2]))
            if len(temp_enermy) != 0 :
                find_enermy.append(temp_enermy[0])
        # 현재 archer_case에서의 죽여야할 적들을 찾았다.
        # 이제 한번에 콱 죽여버리자!
        for f_e in find_enermy:
            d,r,c = f_e
            if temp_graph[r][c] == 1 :
                temp_graph[r][c] = 0
                case_remove += 1
        find_enermy = []

        # 죽이는 것 까지 완료했다.
        # 그럼 한 row씩 이동하자.
        temp_graph.pop()
        temp_graph = [[0 for _ in range(M)]] + temp_graph

    #이제 케이스가 끝나면 max_remove와 비교해보자.
    max_remove = max(max_remove,case_remove)
print(max_remove)