# 220907
"""
소가 10마리 있고, 길은 0,1 둘 중 하나이다.
같은 번호의 소가 위치를 바꾼게 몇번인가??
소가 최소 몇번 길을 건넜나??

"""

N = int(input())
cows_loc = [[0,0] for _ in range(11)]
changes = 0
for _ in range(N):
    cow,loc = map(int,input().split())

    # 첫번째 값은 변화한 적이 있는지 체크하는 것
    if cows_loc[cow][0] == 0 :
        cows_loc[cow][1] = loc
        cows_loc[cow][0] = 1
    else :
        if cows_loc[cow][1] != loc :
            changes +=1
            cows_loc[cow][1] = loc
print(changes)



# 220801
# N = int(input())
# cow_dict = {}
# count = 0
#
# for _ in range(N):
#     cow,loc = map(int,input().split())
#
#     if cow_dict.get(cow) is None :
#         cow_dict[cow] = loc
#     # 이제 소가 길을 건너는지 확인하자.
#     else :
#         before_loc = cow_dict[cow]
#
#         # 위치가 바뀌었으면 count를 세자
#         if before_loc !=  loc :
#             count += 1
#
#         # 다시 갱신
#         cow_dict[cow] = loc
#
# print(count)