"""

 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다.
 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.

컨베이어벨트
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
  - 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.

"""

from collections import deque
N,K = map(int,input().split())
up_belt = deque()
down_belt = deque()
arr = list(map(int,input().split()))
len_arr = len(arr)
for i in range(len_arr):
    if i < len_arr/2 :
        up_belt.append(arr[i])
    else :
        down_belt.appendleft(arr[i])

robots = deque([[0] for _ in range(len_arr//2)])

# 순서는 1,2,3,4 지만 사실 아직 로봇이 올라가있지 않기 때문에,
# 3부터 시작하자.

step = 1
while True :


    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전한다.

    # 먼저 벨트부터 구현하자.
    # up_belt의 마지막이 down belt의 제일 마지막으로.
    down_belt.append(up_belt.pop())
    # down belt의 첫번째가 up belt의 첫번쨰로
    up_belt.appendleft(down_belt.popleft())

    # 그리고 로봇도 한칸씩 이동하자.
    robots.pop() # 이 때의 robots는 마지막 칸에 로봇이 있을 수 없음.
    robots.appendleft([0]) # 첫번째를 빈칸으로 만들어주기.

    """
    마지막 칸에 로봇이 도착했으면 내리자.
    """
    if robots[-1] == [1] :
        robots[-1] = [0]

    # print("step : {}-1 벨트가 이동".format(step))
    # print(robots)
    # print(up_belt)
    # print(down_belt)
    # print("------------")


    # 2. 로봇의 우측부터 확인해서 이동할 수 있으면 이동하자.
    for i in range(len_arr//2-2,-1,-1):
        # 로봇의 오른쪽에 위치한 박스의 내구도를 살피자.
        if up_belt[i+1] != 0 and robots[i+1] == [0] and robots[i] == [1] : # 내구도가 0이 아니고, 로봇의 옆칸이 빈칸이고 지금 위치에 로봇이 있다면
            # 한칸 간다.
            robots[i] = [0]
            robots[i+1] = [1]
            up_belt[i+1] -= 1

        else :
            continue

    """
    마지막 칸에 로봇이 도착했으면 내리자.
    """
    if robots[-1] == [1] :
        robots[-1] = [0]
    #
    # print("step : {}-2 로봇이 움직임".format(step))
    # print(robots)
    # print(up_belt)
    # print(down_belt)
    # print("------------")

    # 3. 올리는 위치의 내구도가 0이 아닌지 확인.
    if up_belt[0] == 0 : # 내구도가 0이면 로봇을 올리지 않는다.
        pass
    else : # 내구도가 0이 아니면 로봇을 올리자.
        robots[0] = [1]
        up_belt[0] -= 1


    # print("step : {}-3 내구도 체크 후 올리기".format(step))
    # print(robots)
    # print(up_belt)
    # print(down_belt)
    # print("------------")

    # 내구도 칸이 0인 칸의 개수가 K개 이상이면 종료.
    cnt = 0
    for a in up_belt :
        if a == 0 : cnt += 1
    for b in down_belt :
        if b == 0 : cnt += 1
    if cnt >= K :
        print(step)
        break
    step+=1
