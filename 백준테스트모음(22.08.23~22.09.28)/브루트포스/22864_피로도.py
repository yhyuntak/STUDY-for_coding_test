"""
하루 1시간 일하면 -> 피로도 A 쌓이고 B만큼 일 처리
하루 1시간 쉬면 피로도 c 삭제
피로도가 최대 M을 넘지 말라.

하루는 24시간이다.

"""

import sys
read= sys.stdin.readline

A,B,C,M = map(int,read().split())

hour = 0
fatigue = 0
work = 0

while hour != 24:
    if fatigue + A <= M :
        fatigue += A
        work += B
    else :
        fatigue -= C

    if fatigue < 0 :
        fatigue = 0
    hour += 1

print(work)