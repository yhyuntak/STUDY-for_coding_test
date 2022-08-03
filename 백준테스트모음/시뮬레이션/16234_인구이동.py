import math
import sys
read =sys.stdin.readline
from fractions import Fraction
from collections import deque

def solution(N,L,R,graph):

    # 상 하 좌 우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # 아 이문제 하루에 다 이동하고 다음날에 다 이동하고 이런느낌이네;
    # 매일 매일 모든 연합을 미리 지정해야함!
    # 그니까 BFS로 매일 연합이 되는 것들을 찾고 저장한다.
    # 근데 저장된 연합이 없다면 그대로 알고리즘 종료. 이런느낌으로 가야할듯.

    union_exist = True

    # 인구이동의 날짜를 세는 count변수 생성
    days = 0

    while union_exist :

        union_space = []
        visited = [[0 for _ in range(N)] for _ in range(N)]

        # 일단 2중 for문으로 모든 곳을 돌아봐야함.
        for r in range(N):
            for c in range(N):

                # 여기서 중요한건, 이미 연합이 되어서 visited 처리가 된 곳은 다시 둘러볼 필요가 없다는 것.

                if visited[r][c] == 1 :
                    continue

                # 현재 위치가 탐색되지 않았다면 이곳을 시작으로 BFS를 진행해서 연합을 찾아보자.

                q = deque()
                q.append([r,c])

                # 현재 위치에서의 연합을 저장할 곳을 임시로 생성
                temp_neighbor = [[r,c]]

                while q :
                    # 현재 위치 뽑기
                    now_r,now_c = q.popleft()
                    # 방문 처리
                    visited[now_r][now_c] = 1

                    # 현재 위치를 기점으로 상하좌우를 탐색하자
                    for i in range(4):
                        search_r = now_r + dy[i]
                        search_c = now_c + dx[i]

                        # 확인할 곳이 일단 정상적인 범위인지 체크하고, 방문한 곳이 아닌지도 함께 체크
                        if (0<= search_r < N and 0<= search_c < N) and visited[search_r][search_c] == 0:
                            # 국경선이 열린게 하나라도 있어야지 인구이동을 할 수 있다.
                            # now와 search의 차이를 확인하자.

                            # L R 범위에 들어간다면
                            if L<= abs(graph[search_r][search_c] - graph[now_r][now_c])<=R :

                                # 현재 위치의 연합국가로 설정
                                temp_neighbor.append([search_r,search_c])
                                # 설정함과 동시에 다시 해당 국가의 주변에 가능한 곳이 있는지 파악하기 위해
                                # queue에 넣고, 다시 방문하지 않기 위해 visited 처리.
                                q.append([search_r,search_c])
                                visited[search_r][search_c] = 1

                if len(temp_neighbor) > 1 :
                    union_space.append(temp_neighbor)

        # 이제 연합들의 묶음이 완성되었으니, 각 연합들 마다 인구 이동을 진행하자.
        # 저장된 연합이 없으면 종료
        if len(union_space) == 0:
            union_exist = False
        # 연합이 있으면 인구이동을 진행하자.
        else :
            #먼저 days를 올리자.
            days +=1
            # 연합을 뽑아서 인구이동 하자.
            for union in union_space :

                # 인구를 모두 더하기
                people = 0
                for union_r,union_c in union :
                    people += graph[union_r][union_c]

                # 인구의 총 합에 근접국의 수를 나누자.
                people = math.floor(Fraction(people,len(union)))
                # 분배하자.
                for union_r,union_c in union :
                    graph[union_r][union_c] = people

    return days


N,L,R = map(int,read().split())
graph = []

for n in range(N):
    graph.append(list(map(int,read().split())))

print(solution(N,L,R,graph))
