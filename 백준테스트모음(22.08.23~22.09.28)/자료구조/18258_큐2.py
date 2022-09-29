import sys
read = sys.stdin.readline
from collections import deque


def f_pop(q):
    if len(q) == 0 :
        return q,-1
    else :
        val = q.popleft()
        return q,val
def f_front(q):
    if len(q) == 0:
        return -1
    else :
        return q[0]
def f_back(q):
    if len(q) == 0:
        return -1
    else :
        return q[-1]

N= int(read())
q = deque()
for _ in range(N):
    temp = list(read().split())
    state = temp[0]

    if state == "push" :
        q.append(temp[1])
    elif state == "pop":
        q,temp_val = f_pop(q)
        print(temp_val)
    elif state == "size":
        print(len(q))
    elif state == "empty":
        if len(q) == 0 :
            print(1)
        else :
            print(0)
    elif state == "front":
        print(f_front(q))
    elif state == "back":
        print(f_back(q))
