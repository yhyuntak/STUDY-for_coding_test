# 220916

# 수가 10보다 작으면 앞에 0을 붙여 두자리수로, 그다음 더해 원래 수의 오른쪽이랑 구한 합의 오른쪽 자리수를 이어붙여라. 사이클의 길이를 구하라

N = int(input())

cycle = 0
save_N = N

while True :
    str_N = str(N)
    if len(str_N) == 1 :
        left,right = '0',str_N
    else :
        left,right = str_N[0],str_N[1]

    temp_sum = str(int(left)+int(right))
    if len(temp_sum) == 1 :
        new_N = ''.join([right,temp_sum])
    else :
        new_N = ''.join([right,temp_sum[1]])

    N = int(new_N)
    cycle += 1
    if N == save_N :
        print(cycle)
        break











# 220801
# N = input()
# cycle = 0
#
# original_N = N
#
# while True :
#
#
#     if len(N) < 2 : N = '0'+N
#     temp_sum = str(int(N[0]) + int(N[1]))
#     new_num = N[-1] + temp_sum[-1]
#     N = new_num
#     cycle+=1
#     if int(original_N) == int(N):  break
#
# print(cycle)