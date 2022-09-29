# 220912

import sys
read = sys.stdin.readline
n = int(read())

"""
q**2 >= n인 최소의 q를 구하라.
"""

start = 0
end = n

while start <= end :
    mid = (start+end)//2

    if mid**2 >= n :
        end = mid - 1

    else :
        start = mid + 1

print(start)

# 220801

# import sys
# read = sys.stdin.readline
#
# N = int(read())
#
# start = 0
# end = N
#
# while start <= end :
#
#     mid = (start+end)//2
#     if mid**2 == N :
#         start = mid
#         break
#
#     elif mid**2 > N : # 더 줄여야한다 mid를
#         end = mid-1
#     else : # mid를 더 키워야한다.
#         start = mid +1
#
# print(start)