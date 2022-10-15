

"""

둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.

1번은 5번에서 결과가 나타나는듯.

2. 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
물고기의 냄새는 아래 3에서 설명한다.

3. 물고기는 8방향이고 상어는 4방향이다. 상어는 연속해서 3칸, 물고기는 1칸이네
상어는 가다가 격자를 벗어나는 길이 있으면, 불가능한 이동 방법이라고 본다.
상어가 이동하던 중 물고기를 만나면 그 칸에 있는 물고기는 전부 삭제 -> for문 이용할 것
제외되는 모든 물고기는 물고기 냄새를 남긴다 -> 횟수도 같이 저장.

가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며,
그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다
사전 순에 대한 문제의 하단 노트에 있다.

4. 두번전 연습에서 생긴 물고기의 냄새는 격자에서 사라진다.

5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
"""

"""
격자에 있는 물고기의 위치, 방향 정보와 상어의 위치, 그리고 연습 횟수 S가 주어진다. 
S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.
"""
from collections import deque
from copy import deepcopy
M,S = map(int,input().split())
fishes = [[deque() for _ in range(4)] for _ in range(4)]
smells = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fx,fy,d = map(int,input().split())
    fishes[fx-1][fy-1].append(['f',d-1])
sr,sc = map(int,input().split())
shark_rc = [sr-1,sc-1]
# fishes[sr-1][sc-1].append(['s',-1])

# 물고기 방향 좌 좌상 상 우상 우 우하 하 좌하
f_dr = [0,-1,-1,-1,0,1,1,1]
f_dc = [-1,-1,0,1,1,1,0,-1]

# 상어 방향 상 좌 하 우
s_dr = [-1,0,1,0]
s_dc = [0,-1,0,1]

def dfs(move_list,sr,sc,move_cnt,eat_cnt) :

    if move_cnt == 0 :
        global max_fish,shark_rc,visit_list
        # print(move_list,dict_min,eat_cnt,max_fish)
        # 움직임이 끝났을 때, 물고기 수가 가장 많은게 첫번째,
        if max_fish < eat_cnt : # 먹은게 저장된 것보다 크면, 모든 맵들, 상어 위치 갱신

            shark_rc = [sr,sc]
            max_fish = eat_cnt
            visit_list = move_list[:]
        return

    for ii in range(4):
        n_sr,n_sc = sr+s_dr[ii],sc+s_dc[ii]
        if 0<=n_sr<4 and 0<= n_sc < 4 : # 상어는 격자 안에만.
            if [n_sr,n_sc] not in move_list :
                move_list.append([n_sr,n_sc])
                dfs(move_list,n_sr,n_sc,move_cnt-1,eat_cnt+len(fishes[n_sr][n_sc]))
                move_list.pop()
            else : # 방문 한적이 있다면,
                dfs(move_list,n_sr,n_sc,move_cnt-1,eat_cnt)
print_bool = False

for s in range(S):

    if print_bool :
        print("start {}".format(s+1))
        print("물고기 맵")
        for _ in range(4):
            print(fishes[_])
        print()
        print("냄새 맵")
        for _ in range(4):
            print(smells[_])
        print('-'*10)

    """
    1) 복제 마법 
    현재 상태의 물고기의 위치와 방향을 5)에서 그대로 표현해야한다.
    """
    for_five_fishes = deepcopy(fishes)

    if print_bool :
        print("STEP 1 : 복제 저장")
        print()

    """
    2) 물고기가 한칸 이동한다. 
    """
    save_fishes_ = deepcopy(fishes)
    fishes = [[deque() for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):

            # 물고기가 존재한다면 상어칸, 냄새칸, 격자범위 벗어나지 않는 곳으로 간다.
            while save_fishes_[r][c] :

                now_kind,now_d = save_fishes_[r][c].pop()
                for i in range(now_d,now_d-8,-1):
                    i %=8
                    nr,nc = r+f_dr[i] , c+f_dc[i]
                    if  (0<=nr<4 and 0<=nc<4) and [nr,nc] != [shark_rc[0],shark_rc[1]] and \
                           not smells[nr][nc] :
                        fishes[nr][nc].append([now_kind, i])
                        break
                else :
                    fishes[r][c].append([now_kind,i])

    if print_bool :
        print("STEP 2 - 물고기 이동")
        print("물고기 맵")
        for _ in range(4):
            print(fishes[_])
        print('-'*10)


    shark_r,shark_c = shark_rc
    max_fish = -1
    visit_list = []
    dfs([],shark_r,shark_c,3,0)

    for vr,vc in visit_list :
        if fishes[vr][vc] :
            smells[vr][vc] = 2 # 냄새 추가하기.
            fishes[vr][vc] = deque() # 물고기 먹기


    if print_bool :
        print("STEP 3 - 상어 이동")
        print("물고기 맵")
        for _ in range(4):
            print(fishes[_])
        print("냄새 맵")
        for _ in range(4):
            print(smells[_])
        print()
        print("상어 위치 : ",shark_rc)
        print('-'*10)

    """
    4) 모든 칸을 확인해서 냄새가 2개 전인 (-2) 것들은 삭제.
    """
    for r in range(4):
        for c in range(4):
            if smells[r][c] :
                smells[r][c] -= 1

    if print_bool :
        print("STEP 4 - 냄새 제거")
        print("냄새 맵")
        for _ in range(4):
            print(smells[_])
        print('-'*10)

    """
    5) 물고기 복제 하기.
    """
    for r in range(4):
        for c in range(4):
            fishes[r][c] = for_five_fishes[r][c]+fishes[r][c]

    if print_bool :
        print("STEP 5 - 물고기 복제")
        print("물고기 맵")
        for _ in range(4):
            print(fishes[_])
        print('-'*10)

sums = 0
for r in range(4):
    for c in range(4):
        sums += len(fishes[r][c])

print(sums)