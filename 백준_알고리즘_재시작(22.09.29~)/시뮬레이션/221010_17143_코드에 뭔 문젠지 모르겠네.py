"""
상어는 최대 한마리.
크기와 속도를 갖고있음.

낚시왕은 0,-1에 있음.
0,C에 도착하면 이동을 멈춤.

1. 한칸 이동
2. 해당 열의 가장 작은 row에 있는 상어를. 잡으면 상어가 사라짐.
3. 상어들 이동

이동하려는 칸이 격자판을 넘어가면 방향을 바꿔서 속력으로 가기.

방향은 상하우좌로 1,2,4,3를 의미.

상어가 이동한 후에 두마리 이상있을때 크기가 가장 큰 것이 나머지를다 잡아먹는다.

낚시왕이 모든 열을 돌면서 잡은 상어의 크기 합은?
"""

R,C,M = map(int,input().split())
graph = [[0 for _ in range(C)] for _ in range(R)]
sharks = [[[] for _ in range(C)] for _ in range(R)]
# 상어는 최대 10000마리까지.
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    sharks[r-1][c-1].append([s,d,z])# r,c,s:속력,d:이동방향,z:크기)
    # if d == 2 :
    #     sharks[r-1][c-1].append([s,2,z])# r,c,s:속력,d:이동방향,z:크기)
    # elif d == 3 :
    #     sharks[r - 1][c - 1].append([s, 1, z])  # r,c,s:속력,d:이동방향,z:크기)
    # elif d == 4 :
    #     sharks[r - 1][c - 1].append([s, 3, z])  # r,c,s:속력,d:이동방향,z:크기)
    # else :
    #     sharks[r - 1][c - 1].append([s, 0, z])  # r,c,s:속력,d:이동방향,z:크기)

# 상 하 우 좌 1 2 3 4
dr = [0,-1,1,0,0]
dc = [0,0,0,1,-1]

# # 상 우 하 좌 0 1 2 3
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]


get_sharks = []

# 낚시왕이 모든 열을 돌 것임.
for person_col in range(C):
    for _ in range(R):
        print(sharks[_])
    # 해당 열에 상어를 확인.
    for s_r in range(R) :
        if sharks[s_r][person_col] != [] : # 상어가 있다면
            # 상어 제거하기.
            temp_get = sharks[s_r][person_col].pop()
            get_sharks.append(temp_get)
            break # 그리고 멈추기.
        # 상어가 없으면 그냥 for문이 돌고 끝.

    """        
    3. 상어들 이동    
    """
    # 일단은 빠르게 이중 루프로 상어들을 파악하고 queue에 넣어서 한번에 처리하자. 그래야 한칸에 둘이 들어가는 것을 확인 가능.

    check_sharks = []
    for r in range(R):
        for c in range(C):
            if sharks[r][c] != [] : # 상어가 있다면
                # 상어 제거해두기.
                temp_get = sharks[r][c].pop()
                check_sharks.append([r,c]+temp_get)


    # 상어가 한턴에 다 움직이자.
    # 움직인 상어를 저장하는 것은 dict으로 처리하자.
    moved_sharks = {}
    while check_sharks :
        r,c,s,d,z = check_sharks.pop() # r,c,s:속력,d:이동방향,z:크기
        """
        이동하려는 칸이 격자판을 넘어가면 방향을 바꿔서 속력으로 가기.    
        방향은 상하좌우로 1,2,3,4를 의미.    
        상어가 이동한 후에 두마리 이상있을때 크기가 가장 큰 것이 나머지를다 잡아먹는다.
        """
        nr,nc = r+dr[d]*s,c+dc[d]*s  # 초기 위치 생성
        while True : # s에 따라서 몇번씩 값을 체크해야함. 어쩔수 없이 while을 써야해.
            # 단순히 방향과 위치를 정해주는 무한루프임.
            # 상 하 우 좌 1 2 3 4
            # dr = [0, -1, 1, 0, 0]
            # dc = [0, 0, 0, 1, -1]
            # print("r:{} c:{} dr:{} dc:{} s:{} d:{} ".format(r,c,dr[d],dc[d],s,d))
            # print("before - nr:{} nc:{} ".format( nr,nc))
            if 0<= nr < R and 0<= nc < C : # 그래프 내에 있을 경우엔
                # 상어는 자리를 이동할 수 있으니 방향은 그대로 이동해야하므로 루프 끝내기.
                break
            # 그래프 내에 없으면 방향을 바꿔야함.  근데 음수로 가면 절댓값을 씌우면 되고.
            elif nr < 0 : # d == 1 일때 밖에 없음
                d += 1
                nr = abs(nr)
            elif nc < 0 : # d == 4 일때 밖에 없음.
                d -= 1
                nc = abs(nc)
            elif nr >= R : # d == 2 일때 밖에 없음.
                d -= 1
                nr = 2*(R-1)-nr
            elif nc >= C : # d == 3 일때 밖에 없음
                d += 1
                nc = 2*(C-1)-nc

        try:
            # 상어가 두마리 있다면 크기를 비교해서 미리 상어를 제거하는게 효율적.
            present = moved_sharks[(nr, nc)].pop()
            if present[-1] > z : # 현재 상어가 더 크면 다시 얘만 넣기.
                moved_sharks[(nr,nc)].append(present)
            else : # 아니라면 새로운 상어가 먹는다.
                moved_sharks[(nr, nc)].append([s, d, z])
        except:
            # 상어가 한마리만 있으면 그냥 저장하면 됌
            moved_sharks[(nr, nc)] = [s, d, z]
            # print("after - nr:{} nc:{} ".format( nr,nc))

    for loc,val in list(moved_sharks.items()):
        sharks[loc[0]][loc[1]].append(val)

results = 0
for shark in get_sharks :
    results += shark[-1]
print(results)