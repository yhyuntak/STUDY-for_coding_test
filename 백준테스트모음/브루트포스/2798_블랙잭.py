# 220912

"""
카드 합이 21을 넘지 않는 한도내에 합을 최대로 만들면 승리

"""

from itertools import combinations

N,M = map(int,input().split())
array = list(map(int,input().split()))
differ = 10e9
answers = 0
for a in list(combinations(array,3)) :
    temp = sum(a)
    if temp <= M :
        if M - temp < differ :
            answers = temp
            differ = M - temp
print(answers)