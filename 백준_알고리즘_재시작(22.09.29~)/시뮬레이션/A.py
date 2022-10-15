from collections import deque

N = 8

arr = []

def dfs(n):

    if len(arr) == N//2 :
        print(arr)
        return

    for i in range(n,min(N//2+n +1,N+1) ) :
        arr.append(i)
        dfs(i+1)
        arr.pop()

for j in range(1,N//2+1):
    arr.append(j)
    dfs(j+1)
    arr.pop()


# from collections import deque
#
#
# N = 8
#
# star = deque([i for i in range(1,N+1)])
# link = deque()
#
# def dfs(n):
#
#     if len(a) == 4 :
#         print(a)
#         return
#
#
#     for i in range(N//2+len(link)):
#
#         a.append(i)
#         dfs(i+1)
#         a.pop()
#
#
#
# for j in range(1,N//2+1):
#
#     link.append(star.popleft())
#     dfs(j)
#     star.append(link.pop())