"""

총 8개의 톱니를 가진 바퀴가 4개가 있다.
각 톱니는 N또는 S극을 나타낸다. 순서대로 1,2,3,4 바퀴이다.

톱니를 K번 회전시킨다. 시계 반시계가 있다.

톱니를 회전시킬꺼면 톱니바퀴와 방향을 설정해야. 맞닿은 극에따라서 톱니를 회전시키룻도 있고 안할수도있는데, 맞닿은 극이 다르면 당한 바퀴는 가한 바퀴의 반대 방향으로 회전한다.

연쇄작용이다.

"""


# 바퀴 상태는 12시부터 시계방향으로 주어짐. n극은 0, s극은 1
wheels = []

for _ in range(4):
    temp = input().split()
    temp = temp[0]
    temp_list = [ int(t) for t in temp]
    wheels.append(temp_list)

K = int(input())

def check_face():
    info = [[False],[],[],[]]
    if wheels[0][2] == wheels[1][6] :
        info[0].append(False)
        info[1].append(False)
    else :
        info[0].append(True)
        info[1].append(True)

    if wheels[1][2] == wheels[2][6] :
        info[1].append(False)
        info[2].append(False)
    else :
        info[1].append(True)
        info[2].append(True)

    if wheels[2][2] == wheels[3][6] :
        info[2].append(False)
        info[3].append(False)
    else :
        info[2].append(True)
        info[3].append(True)

    info[3].append(False)

    return info

def clockwise(array):
    # 한칸씩 오른쪽으로
    temp_array = array[:-1]
    array = [array[-1]] + temp_array
    return array

def counter_clockwise(array):
    # 한칸씩 왼쪽으로
    temp_array = array[1:]
    array = temp_array + [array[0]]
    return array

def rotation(array,rot):
    if rot == 1 : # cw
        return clockwise(array)
    else :
        return counter_clockwise(array)


from collections import deque

for _ in range(K):
    # 이제 여기에 시뮬레이션을 생성하자
    # 1번의 idx 2과 2번의 idx 6이 맞물림
    # 2번의 idx 2과 3번의 idx 6이 맞물림
    # 3번의 idx 2과 4번의 idx 6이 맞물림
    # 항상 이게 맞물려있는지 확인을 미리 해놓을까?

    # 리스트의 정보는 1과2, 2와3, 3과4의 맞닿은 상태가 같으면 True 아니면 False를 갖는다.
    face_info = check_face()
    num, rot = map(int, input().split())
    num = num-1 # 인덱스 헷갈린다.
    visited = [0,0,0,0]
    q = deque()
    q.append([num,rot])
    visited[num] = 1
    dn = [-1,1]

    turn_info = [[num,rot]]
    while q :
        now_num,now_rot = q.popleft()
        # for문을 통해서 현재 바퀴의 좌 우를 확인한다.
        # for i in range(2):
        #     next_num = now_num+dn[i]
        #     if 0< next_num <= 4 :
        #         if face_state
        #         visited[next_num-1] = 1

        for idx,face_state in enumerate(face_info[now_num]):
            if idx == 0 : # 왼쪽으로
                move = -1
            else : # 오른쪽으로
                move = 1
            next_num = now_num + move
            if face_state and visited[next_num] == 0: # 돌아가야 하는 바퀴면서 방문하지 않았다면 queue에 추가.
                q.append([next_num,now_rot*-1])
                turn_info.append([next_num,now_rot*-1])
                visited[next_num] = 1

    # 이제 turn_info에 따라서 바퀴들을 회전시켜주면 된다. 이때 순서는 상관없다.
    for num_wheel,rot_state in turn_info :
        wheel_array = wheels[num_wheel]
        wheel_array = rotation(wheel_array,rot_state)
        wheels[num_wheel] = wheel_array
# 마지막으로 각 바퀴들의 12시방향의 극을 측정해서 점수 매기기
sums = 0
for i in range(4):
    if wheels[i][0] == 1 :
        sums += 2**i
print(sums)