# 220912
"""
AAAA,BB가 있음
x를 위 두 카드로 덮을 것임
.은 그냥 쓰고
덮어지지 않는다면 포기할것!
"""

# 먼저 A로 다 덮고 나머지를 B로 덮는 방식을 택하자. 왜냐하면 BB를 두개 쓰는 것은 AAAA로 커버가 가능하기 때문이다.

problem = input()

num_of_X = 0
success = 0
save_array = []
array_AAAA = ['AAAA']
array_BB = ['BB']
for p in problem :
    if p == "X" :
        num_of_X += 1
    else :
        # . 을 만나면 어떤 이벤트가 발생
        # 먼저 . 앞에 x의 수를 세서 그 x가 홀수면 바로 -1을 출력하고 break
        if num_of_X % 2 == 1 :
            success = 0
            break

        # x가 짝수면 4로 최대한 나누자.
        else :
            num_of_A = num_of_X // 4
            num_of_X %= 4
            num_of_B = num_of_X // 2
            num_of_X = 0
            success = 1
            save_array = save_array + array_AAAA*num_of_A + array_BB*num_of_B + ['.']


# X로 끝나는 경우 한번더 확인
if num_of_X % 2 == 1 :
    success = 0
# x가 짝수면 4로 최대한 나누자.
else :
    num_of_A = num_of_X // 4
    num_of_X %= 4
    num_of_B = num_of_X // 2
    num_of_X = 0
    success = 1
    save_array = save_array + array_AAAA*num_of_A + array_BB*num_of_B

if success == 0 :
    print(-1)
else :
    for save in save_array :
        print(save,end="")

# 220801
# def solution():
#
#     input_list = list(input().split())
#
#     # 하나씩 확인하면서, X인 부분들을 찾는 느낌.
#     save_space = []
#     result_list = []
#     count = 0
#     for idx,t in enumerate(input_list[0]) :
#         # . 를 만나면 어떤 작업을 하자.
#         if t == '.' :
#
#             result = []
#             if count % 2 == 1 :
#                 return -1
#             # 사전순으로 빠르게 배열해야하니 A가 무조건 앞에 와야댐.
#             # 그럴려면 count가 4로 나눴을 때 몫이 존재해야함.
#             # 그만큼 AAAA를 넣어주면 됨.
#             if count > 0 :
#                 four = count//4
#                 two = (count-four*4)//2
#                 four_list = ['AAAA' for _ in range(four)]
#                 two_list = ['BB' for _ in range(two)]
#
#                 result.append(''.join(four_list))
#                 result.append(''.join(two_list))
#             result.append('.')
#             result_list.append(''.join(result))
#             count = -1
#         count+=1
#
#         if idx == len(input_list[0])-1 :
#
#             result = []
#             if count % 2 == 1 :
#                 return -1
#             # 마지막에 .을 못만나고 끝날수도. 그럼 그땐 이렇게
#             four = count//4
#             two = (count-four*4)//2
#             four_list = ['AAAA' for _ in range(four)]
#             two_list = ['BB' for _ in range(two)]
#
#             result.append(''.join(four_list))
#             result.append(''.join(two_list))
#             result_list.append(''.join(result))
#     last_result = ''.join(result_list)
#     return last_result
# print(solution())