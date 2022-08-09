"""
임의의 수열이 주어지고,
<<연속된>>몇개의 수를 선택해 구할 수 있는 것중 가장 큰 합을 구하자.
정렬은 안하는 듯.
"""

import sys
read = sys.stdin.readline
N = int(read())
array = list(map(int,read().split()))

"""
자기자신 vs 자기 전의 것과 더한 것을 비교하면 알아서 될듯.
"""

dp_table = [0 for _ in range(N)]

dp_table[0] = array[0]

for i in range(1,N):
    now = array[i]
    dp_table[i] = max(now,dp_table[i-1]+now)

print(max(dp_table))