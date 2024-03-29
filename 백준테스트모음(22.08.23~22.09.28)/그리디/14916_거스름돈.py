# 220906
# 동전의 최소개수

n = int(input())
coins = [2,5]

max_iter = n // 5
results_save = []
if n % 2 == 0 :
    results_save.append(n//2)
    min_val = n//2
else :
    results_save.append(-1)
    min_val = 10e9

for iter in range(1,max_iter+1):
    temp_n = n - iter*5
    if temp_n % 2 == 0:
        results_save.append(temp_n // 2)
        min_val = min(min_val,temp_n // 2 + iter)
    else:
        results_save.append(-1)
if results_save.count(-1) == len(results_save) :
    print(-1)
else :
    print(min_val)

# # 거스름돈 2,5로만
# # 동전 개수 최소로
# # 거스름돈은 n임
# # 최소 동전의 개수는?
#
# # 문제 풀이
# # 5로 먼저 나누고 2로 나눈다
#
# N = int(input())
# results = []
# coins = [5,2]
#
# # 5를 최대한 사용 가능한 횟수 K
# K = N//5
#
# if K == 0 :
#     temp = N // 2
#     if N % 2 > 0 :
#         print(-1)
#     else :
#         print(temp)
#
# else :
#     min_val = 1e9
#     for i in range(0,K+1):
#         # 5원의 개수 : i
#         two_temp = (N - 5*i) // 2 # 2원의 개수 : two_temp
#         if (N - 5*i) % 2 == 0 : # 딱 계산 가능하면
#             min_val = min(min_val,i+two_temp)
#             # results.append(i+two_temp)
#     if min_val == 1e9 :
#         print(-1)
#     else :
#         print(min_val)