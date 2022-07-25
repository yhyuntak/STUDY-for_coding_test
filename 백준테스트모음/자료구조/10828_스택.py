import sys

def push_func(array,n):
    array.append(int(n))
    return array
def pop_func(array):
    if len(array) > 0 :
        temp = array.pop()
        return array, temp
    else :
        return [],-1
def size_func(array):
    return len(array)
def empty_func(array):
    if len(array) == 0 :
        return 1
    else :
        return 0
def top_func(array):
    if len(array) == 0 :
        return -1
    else :
        return array[-1]

read = sys.stdin.readline
N = int(read())
# 각 입력을 받고 저장하기보단 N이 최대 10000이므로, 매 반복마다 함수 실행을하자.
results = []
array = []
for _ in range(N):
    temp = list(read().split())
    # print(temp,array)
    if temp[0] == "push":
        array = push_func(array,temp[1])
    elif temp[0] == "pop":
        array,val = pop_func(array)
        if len(array) == 0 :
            print(val)
        else :
            print(val)
    elif temp[0] == "size":
        print(size_func(array))

    elif temp[0] == "empty":
        print(empty_func(array))

    elif temp[0] == "top":
        if top_func(array) == -1 :
            print(-1)
            array = []
        else :
            print(top_func(array))
