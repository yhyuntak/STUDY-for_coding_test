
다시풀기


# 
# import sys
# read = sys.stdin.readline
# 
# N = int(read())
# schedules = [[]] # 헷갈리지 않게 1일부터 시작하게 하자.
# for _ in range(N):
#     schedules.append(list(map(int,read().split())))
# 
# d = [ 0 for _ in range(N+1)]
# max_val = 0
# for day in range(1,N+1):
#     g = schedules[day]
#     max_val = max(max_val,d[day])
#     if day + g[0] > N :
#         continue
#     d[g[0]+day] = max(max_val+g[1],d[g[0]+day])
# print(max(d))
# 
# 
