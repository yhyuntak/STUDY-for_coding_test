"""

구역을 5개로 나눠야하낟.

각 구역은 무조건 선거구들 중 하나에 포함되어야함.

선거구는 적어도 구역 하나를 포함해야하고, 각 구역들은 인접해 있어야한다.

경계선을 포함한 내부 지역은 5번 선거지역이다.

구역 (r, c)의 인구는 A[r][c]이고, 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값
선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.
"""

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
region_ = [[0 for _ in range(N)] for _ in range(N)]
import copy
# x,y,d1,d2를 내가 정해야하는듯.

# x,y를 이중 루프로 구현
# 단, 모든 선거구는 적어도 1개 이상의 구역을 가져야하고 d1,d2가 1 이상이므로,
# 범위를 다음과 같이 제한해야한다.[0,1]~[0,N-2],[N-3,1],[N-3,N-2]
# 그리고 경계선도 항상 그래프 안에 존재해야한다.
min_val = 10e9
for r in range(N-2):
    for c in range(1,N-1):
        # d1은 c의 왼쪽에 할 수 있는 만큼을 표현해야하므로,
        for d1 in range(1,c+1): # c가 1이면 d1은 1밖에안되고 2이면 1,2까지 가능..
            # d2는 c의 오른쪽에 할 수 있는 만큼을 표현
            for d2 in range(1,N-c): #이론상 그냥 마지막까진 표현 가능?
                # 그런데 아래에 퍼지는 것도 고려해야한다. 그 기준은 r+d1+d2 <= N , c+d2 <=N임.
                if r+d1+d2 >= N : # 그래프를 벗어남을 표현함
                    continue
                # print("r : {}, c : {}, d1 : {}, d2 : {} ".format(r,c,d1,d2))
                # 여기까지 왔으면 r,c,d1,d2의 set이 완성됬다.
                # 경계선을 포함해서 5번 선거구를 표현해주면 좋을거 같은데

                # row는 r<= <=r+d1+d2까지. col은 c-d1<= <=c+d2 까지.
                # row가 1씩 커지면서 temp_d1,temp_d2에 +1씩 하다가 d1,d2에 걸리면 -1로 할 수 있을까?
                d1_sign = 1
                d2_sign = 1
                temp_d1 = 0
                temp_d2 = 0
                region = copy.deepcopy(region_)
                region[r][c] = 5
                five = A[r][c]
                for r5 in range(r+1,r+d1+d2+1) :
                    temp_d1 += d1_sign
                    temp_d2 += d2_sign
                    if temp_d1 > d1 :
                        d1_sign = -1
                        temp_d1 -= 2
                    if temp_d2 > d2 :
                        d2_sign = -1
                        temp_d2 -= 2
                    # 1씩 더했는데, 만약 d1,d2를 넘어가게 되면 부호를 바꾸고 -하기.
                    for c5 in range(c-temp_d1,c+temp_d2+1):
                        region[r5][c5] = 5
                        five += A[r5][c5]
                #
                # for _ in range(N):
                #     print(region[_])
                #
                # print()
                # 이제 각 선거구의 구역을 파악하면 된다.

                one = 0
                for r1 in range(0, r + d1):
                    for c1 in range(0, c+1):
                        if region[r1][c1] != 5:
                            one += A[r1][c1]
                two = 0
                for r2 in range(0, r + d2+1):
                    for c2 in range(c+1, N):
                        if region[r2][c2] != 5:
                            two += A[r2][c2]
                three = 0
                for r3 in range(r+d1, N):
                    for c3 in range(0, c-d1+d2):
                        if region[r3][c3] != 5:
                            three += A[r3][c3]
                four = 0
                for r4 in range(r+d2+1, N):
                    for c4 in range(c-d1+d2,N):
                        if region[r4][c4] != 5:
                            four += A[r4][c4]

                max_v = max([one, two, three, four, five])
                min_v = min([one, two, three, four, five])

                min_val = min(min_val,(max_v-min_v))
                # print([one, two, three, four, five])
                # print(max_v-min_v)

# print("min : ",min_val)
print(min_val)