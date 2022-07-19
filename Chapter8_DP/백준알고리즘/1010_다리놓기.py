import math

T = int(input())
array = []
#
# def each_product(N):
#     temp = 1
#     for j in range(1,N+1):
#         temp*=j
#     return temp
#

for i in range(T):
    x,y = map(int,input().split())
    val = math.factorial(y)//(math.factorial(y-x)*math.factorial(x))
    array.append(val)

for k in range(T):
    print(int(array[k]))