"""

처음에는 시작 칸에 말 4개가 있다.

화살표대로만 이동 가능.

파란색화살표는
말이 파란색 칸에서 이동을 시작

빨강이는
이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작


말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다. -> 이동중이어도 마칠 수 있는 듯 , 단 사라지는게 아님.

총 10개의 턴이고 주사위는 1~5까지 매턴 굴리기. 도착 칸에 있지 않은걸 하나골라서 주사위 만큼 이동.

만약 말이 이동해서 도착할 곳에 말이 있으면 그건 선택하면 안된다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.

말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.

나올 수 10개를 미리 알고 있을 때, 점수의 최댓값은?
"""

# 빨강은 +2 고
# 파랑은 방향을 바꿔서 간다. 10,20,30 일때를 나눠서 생각해야한다.

# 각 요소들은 뛰어넘는 정도를 표현한다고 생각.
horses = [[0,'all'] for _ in range(4)] # 현재 위치의 인덱스, 현재 맵
from collections import deque
dices = deque(list(map(int,input().split())))

all_map = [2*i for i in range(22)] # 0~42
map_10 = [10,13,16,19,25,30,35,40,45]
map_20 = [20,22,24,25,30,35,40,45]
map_30 = [30,28,27,26,25,30,35,40,45]

def dfs(h,d,sum_val):
    global max_val
    if len(d) == 0 :
        # 주사위를 다 돌렸으면 합을 확인하자.

        return
    # 말 4개가 전부 dice를 가질 수 있다
    for i in range(4):
        now_dice = dices.popleft()
        now_horse_idx,now_horse_map = h[i]
        # 이제 움직임 알고리즘을 만들어야한다.
        # 먼저 현재 말의 위치를 확인한다.
        """
        10,20,30은 시작지점을 확인.
        """
        # 말이 갖고 있는 맵 정보를 확인 (now_horse_map)
        # 이게 'all'일 경우에만 파란색 발판을 밟을 수 있음. 그 외에는 자기 자신의 맵을 따라가면 된다.
        # 'all'인지 파악하자
        if now_horse_map == 'all':
            # 이때만 현재 위치가 파란색 발판인지 확인하자.
            now_horse_loc = all_map[now_horse_idx]

            if now_horse_loc == 10:
                # 10이면 맵 상태를 ten으로 바꾸자.
                now_horse_map = 'ten'
                # 그리고 현재 말의 index도 0으로 초기화 해주자.
                now_horse_idx = 0
            elif now_horse_loc == 20:
                # 20이면 맵 상태를 twenty으로 바꾸자.
                now_horse_map = 'twenty'
                # 그리고 현재 말의 index도 0으로 초기화 해주자.
                now_horse_idx = 0
            elif now_horse_loc == 30:
                # 30이면 맵 상태를 thirty으로 바꾸자.
                now_horse_map = 'thirty'
                # 그리고 현재 말의 index도 0으로 초기화 해주자.
                now_horse_idx = 0

        else :  # 'all'이 아닐 경우에는 바꿔야할지 고민안해도 된다.
            pass

        # 이제 자기 index와 맵이 정해졌으면, 맵에 따라 움직이자.

        # 먼저 인덱스부터 업데이트.
        # 현재 인덱스+주사위 값이 업데이트된 인덱스다
        update_idx = now_horse_idx + now_dice
        """
        말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
        """
        if now_horse_map == 'all' :
            # 만약 업데이트 되는 칸에
            sums.append(all_map[update_idx])
        elif now_horse_map == "ten" :
            sums.append(map_10[update_idx])
        elif now_horse_map == "twenty" :
            sums.append(map_20[update_idx])
        elif now_horse_map == "thirty" :
            sums.append(map_30[update_idx])

        # 값을 저장했으면, 현재 말의 정보도 업데이트
        h[i] = [update_idx, now_horse_map]
        # 아마 여기서 백트래킹 dfs를 적용



max_val = -10e9
# 다같이 시작에서 주사위의 첫번째로 시작하니까. 뭐부터 시작하던 상관 없다. 중복을 없애기 위해서 1번 주사위가 무조건 첫 주사위를 가져간다고 생각하자.
horses[0][0] = dices.popleft() # 인덱스를 저장해놓자.
sums = []
sums.append(all_map[horses[0][0]])
# print(sums)
dfs(horses,dices,sums)

"""
일단 맵에 대해서는, 10,20,30,25,40에 대해선 좀 생각해봐야할듯.
"""
