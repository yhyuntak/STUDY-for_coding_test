import sys
import math
from collections import deque
def first_func(array):

    return round(sum(array)/len(array))

def second_func(array):
    num = len(array)//2#math.ceil(len(array)/2)
    return array[num]

def third_func(counts_dict):

    sorted_list =sorted(counts_dict.items(),key=lambda x:(-x[1],x[0]))

    if len(sorted_list) == 1 :
        return sorted_list[0][0]
    else :
        # 최빈값이 같다면 2번째꺼 출력 :
        if sorted_list[0][1] == sorted_list[1][1] :
            return sorted_list[1][0]
        else :
            return sorted_list[0][0]

def forth_func(array):
    if len(array) == 1 :
        return 0
    else :
        return max(array)-min(array)

if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    sort_list = [0]*(8001)
    array = []
    counts = dict()
    for _ in range(N):
        temp = int(read())
        array.append(temp)
        if not temp in counts :
            # 딕셔너리에 key가 없다면
            counts[temp] = 1
        else :
            counts[temp] += 1

    array.sort()

    print(first_func(array))
    print(second_func(array))
    print(third_func(counts))
    print(forth_func(array))