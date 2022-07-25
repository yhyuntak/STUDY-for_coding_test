import sys
read = sys.stdin.readline
import math

T = int(read())

N_list = list(map(int,read().split()))

min_N = min(N_list)
root_min_N = math.floor(math.sqrt(min_N))

for i in range(1,root_min_N+1):
    

