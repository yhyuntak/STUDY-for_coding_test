"""
전투력 시스템

10000<= WEAK
10000< <=100000 NORMAL
100000< <=1000000 STRONG
"""

import sys
read = sys.stdin.readline
N,M = map(int,read().split())
award_list = []
score_list = []
for _ in range(N):
    award, score = read().split()
    if len(score_list) == 0 or score_list[-1] != score :
        award_list.append(award)
        score_list.append(int(score))

val_list = []
for _ in range(M):
    temp_val = int(read())

    start_idx = 0
    end_idx = len(award_list)-1

    while start_idx <= end_idx :
        mid_idx = (start_idx+end_idx)//2
        if score_list[mid_idx] >= temp_val :
            end_idx = mid_idx - 1
        else :
            start_idx = mid_idx + 1
    print(award_list[start_idx])