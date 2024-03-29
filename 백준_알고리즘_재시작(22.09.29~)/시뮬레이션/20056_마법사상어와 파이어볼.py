"""
1. 파이어볼이 자신의 방향 di로 si만큼 이동
* 이동하는 중 같은 칸에 여러개의 파이어볼이 있을 수 있다.

2. 이동이 끝나고 2개 이상의 파이어볼이 있는 칸에서 아래의 일이 발생
1) 같은 칸의 파이어볼은 합쳐진다
2) 파이어볼은 4개의 볼로 나뉘는데
3) 질량 속력 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
4) 질량이 0인 파이어볼은 삭제

k번 이동한 후, 남아있는 파이어볼의 질량합

"""

# 상 우상 우 우하 하 좌하 좌 좌상 : 1, ... 2 3 4 5 6 7
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

all_fireball = [0,2,4,6]
not_fireball = [1,3,5,7]

N,M,K = list(map(int,input().split()))
graph = [[0 for _ in range(N)] for _ in range(N)]
# fireball은 deque로 해야할듯.
from collections import deque
fireballs = deque()
for _ in range(M):
    fireballs.append(list(map(int,input().split())))

# 파이어볼 정도는 r,c,m,s,d 로 이루어짐
# r:row,c:col,m:mass,s:speed,d:direction

#이제 시작
for k in range(K):
    """
    1. 파이어볼이 자신의 방향 di로 si만큼 이동
        * 이동하는 중 같은 칸에 여러개의 파이어볼이 있을 수 있다.
    """
    # k마다 모든 파이어볼이 한번에 움직인다는 것을 잊지말것.
    moved_dict = {}
    for len_fireball in range(len(fireballs)):
        r,c,m,s,d = fireballs.popleft()
        # 일단 fireball을 이동시키자.
        # 여기서 순환하는 건 %로 구현가능한다.
        next_r = (r+dr[d]*s)%N
        next_c = (c+dc[d]*s)%N
        if moved_dict.get((next_r,next_c)) is None :
            moved_dict[(next_r,next_c)] = [[next_r,next_c,m,s,d]]
        else :
            moved_dict[(next_r, next_c)].append([next_r, next_c, m, s, d])

    moved_fireballs = deque()
    # 이동은 했는데, 2개 이상의 파이어볼이 있는 칸을 찾아야하는데.. dict을 이용해보자
    for loc,info in moved_dict.items():
        # 2개 이상의 파이어볼이 존재한다면
        if len(info) >= 2 :
            # 파이어볼을 합치고
            # 4개의 파이어볼로 나뉠 것인데
            # 나뉜 정보를 fireballs 에 다시 추가하면 될듯
            new_mass = 0
            new_speed = 0
            check_direction = []
            #each_info = [r,c,m,s,d]

            for each_info in info :
                new_mass += each_info[2]
                new_speed += each_info[3]
                check_direction.append(each_info[4]%2)
            new_mass //= 5
            new_speed //= len(info)

            # 질량이 0이 된다면 이 파이어볼은 사라지는 것임
            if new_mass == 0 :
                continue
            else :

                # 홀수 : 1 , 짝수 : 0
                criterion = check_direction[0]
                for i in range(1,len(check_direction)):
                    if criterion == check_direction[i] :
                        continue
                    else :
                        criterion = -1
                        break
                # criterion이 위 과정을 거쳐서 0이 나오면 모두 짝수, 1이 나오면 모두 홀수
                # -1이 나오면 아무것도 아닌것
                if criterion == 1 or criterion == 0 :
                    # 무조건 4개로 쪼개지는 것을 잊지말자.
                    for j in range(4):
                        moved_fireballs.append([loc[0],loc[1],new_mass,new_speed,all_fireball[j]])
                else :
                    for j in range(4):

                        moved_fireballs.append([loc[0], loc[1], new_mass, new_speed, not_fireball[j]])
        else :
            # 2개 미만이면 그냥 fireballs에 현재 파이어볼의 정보를 저장하자.
            moved_fireballs.append(info[0])
    fireballs = moved_fireballs
summations = 0

for _,_,mm,_,_ in fireballs :
    summations += mm
print(summations)


