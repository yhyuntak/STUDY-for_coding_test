import sys
read = sys.stdin.readline

A,B,C,M = list(map(int,read().split()))

hour = 0
fatigue = 0
work = 0
while hour != 24 :

    # 일을 했다고 가정하고 판단하는게 맞는듯.

    # 피로도가 최대를 넘지 않을 때만 일하자.

    if fatigue + A <= M :
        fatigue += A
        work += B
    # 피로도가 최대를 넘으면 쉬자.
    else :
        fatigue -= C

    if fatigue < 0 :
        fatigue = 0
    hour +=1


print(work)