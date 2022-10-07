
"""
높이가 모두 같거나, 경사로를 놓는데 경사로의 높이는 1로만. 길이는 L이다. 개수는 매우 많다.
길이라는게 경사로가 놓이는 바닥의 길이를 얘기하는듯.
한번 놓인 곳은 또 놓을수 없다.
경사로는

"""
import copy
import sys
read = sys.stdin.readline

N , L = map(int,input().split())

my_map = []
for _ in range(N):
    my_map.append(list(map(int,read().split())))

# 자기 주변 탐색하면서 다음 꺼를 탐색하는 순간의 방향을 같이 저장할 필요가 있다.
# 이건 경사로가 놓이는 맵을 생각해야한다.

# 그리고 한번 간 방향은 쭉가면 된다. 이 경우에는 중간 중간은 탐색할 필요가 없다. 첫번째 로우와 컬럼만 보면 된다.

# 먼저 row에 대해서 하고 col에 대해서 하면 될거 같네

# 그리고 이게 최대를 안쓴거 보면 아마 고려하지 않아도 되는 문제인듯.

# 0: col - 하 , 1 : row - 우
dr = [1,0]
dc = [0,1]

from collections import deque

total_road = 0
# side_map = [[0 for _ in range(N)] for _ in range(N)]

"""
column별로 먼저 살펴보기
"""

for c in range(N): # 첫번째 row를 col별로 확인
    new_dict = {}
    now_val = my_map[0][c]
    new_dict[now_val] = 1
    can_go = True
    side_map = [0 for _ in range(N)]
    for next_r in range(1,N): # 쭉 아래로 훑는 걸 구현
        next_val = my_map[next_r][c]
        if now_val == next_val :
            # 값이 같으면 dict에 추가만. 왜냐하면 갑자기 1이 큰 것을 만나면 지금 값들의 길이가 경사로를 놓을 수 있는지 파악하기 위해
            new_dict[next_val] += 1
            continue

        #여기에 애초에 값의 차이가 1인 것만 허용하도록 코딩해야.
        elif abs(now_val-next_val) == 1 :
            if now_val > next_val  : # 현재 높이가 다음 높이보다 더 클 경우 -> 내려가는 경우
                # L만큼 for문을 돌려서 경사로를 놓을 수 있는지 확인하라.
                save_len = 0
                for l in range(0,L):
                    next_r_check = next_r+l
                    if next_r_check < N and side_map[next_r_check] == 0 : # 근데 칸을 벗어나지 않으면서 경사도가 설치되어있지 않은 곳
                        # 칸을 넘지 않았으면 개수를 체크
                        if my_map[next_r_check][c] == next_val :
                            save_len += 1
                            side_map[next_r_check] = 1
                    else :
                        break

                # 만약 save_len이 길이 L과 같다면 무조건 갈 수 있게 됨.
                if save_len == L :
                    # 갈 수 있다면 dict을 초기화 하자.
                    new_dict = {}
                    # 그리고 값을 바꾸기.
                    now_val = next_val
                    new_dict[now_val] = 1

                else : # 같지 않다면, 현재 for문을 종료해서 더이상 탐색할 가치가 없음을 표현하자.
                    can_go = False
                    break

            elif now_val < next_val : # 현재 높이가 다음 높이보다 작을 경우 -> 올라가는 것

                # dict에 저장된 현재 road의 길이를 L과 비교하라.
                if new_dict[now_val] >= L and sum(side_map[next_r-L:next_r])==0 :
                    # 길이가 L 이상이면 dict을 초기화 하자.
                    new_dict = {}
                    # 그리고 값을 바꾸기.
                    now_val = next_val
                    new_dict[now_val] = 1

                else:  # 같지 않다면, 현재 for문을 종료해서 더이상 탐색할 가치가 없음을 표현하자.
                    can_go = False
                    break

        else : # 높이의 차가 1보다 크면 아예 이 col은 더 돌 필요가 없다.
            can_go = False
            break

    # 만약 r이 모든 조건을 끝내고 끝까지 탐색해서 N-1이 되면 그 길은 갈 수 있는 길이다.

    if next_r == N-1 and can_go:
        total_road += 1

"""
이제 row별로 오른쪽들을 확인하자
"""

for r in range(N): # 첫번째 col를 row별로 확인
    new_dict = {}
    now_val = my_map[r][0]
    new_dict[now_val] = 1
    can_go = True
    side_map = [0 for _ in range(N)]
    for next_c in range(1,N): # 쭉 아래로 훑는 걸 구현
        next_val = my_map[r][next_c]
        if now_val == next_val :
            # 값이 같으면 dict에 추가만. 왜냐하면 갑자기 1이 큰 것을 만나면 지금 값들의 길이가 경사로를 놓을 수 있는지 파악하기 위해
            new_dict[next_val] += 1
            continue

        #여기에 애초에 값의 차이가 1인 것만 허용하도록 코딩해야.
        elif abs(now_val-next_val) == 1 :
            if now_val > next_val  : # 현재 높이가 다음 높이보다 더 클 경우 -> 내려가는 경우
                # L만큼 for문을 돌려서 경사로를 놓을 수 있는지 확인하라.
                save_len = 0
                for l in range(0,L):
                    next_c_check = next_c+l
                    if next_c_check < N and side_map[next_c_check] == 0 : # 근데 칸을 벗어나지 않으면서 경사도가 설치되어있지 않은 곳
                        # 칸을 넘지 않았으면 개수를 체크
                        if my_map[r][next_c] == next_val :
                            save_len += 1
                            side_map[next_c_check] = 1
                    else :
                        break

                # 만약 save_len이 길이 L과 같다면 무조건 갈 수 있게 됨.
                if save_len == L :
                    # 갈 수 있다면 dict을 초기화 하자.
                    new_dict = {}
                    # 그리고 값을 바꾸기.
                    now_val = next_val
                    new_dict[now_val] = 1

                else : # 같지 않다면, 현재 for문을 종료해서 더이상 탐색할 가치가 없음을 표현하자.
                    can_go = False
                    break

            elif now_val < next_val : # 현재 높이가 다음 높이보다 작을 경우 -> 올라가는 것

                # dict에 저장된 현재 road의 길이를 L과 비교하라.
                if new_dict[now_val] >= L and sum(side_map[next_c-L:next_c])==0 :
                    # 길이가 L 이상이면 dict을 초기화 하자.
                    new_dict = {}
                    # 그리고 값을 바꾸기.
                    now_val = next_val
                    new_dict[now_val] = 1

                else:  # 같지 않다면, 현재 for문을 종료해서 더이상 탐색할 가치가 없음을 표현하자.
                    can_go = False
                    break

        else : # 높이의 차가 1보다 크면 아예 이 col은 더 돌 필요가 없다.
            can_go = False
            break

    # 만약 r이 모든 조건을 끝내고 끝까지 탐색해서 N-1이 되면 그 길은 갈 수 있는 길이다.

    if next_c == N-1 and can_go:
        total_road += 1
print(total_road)