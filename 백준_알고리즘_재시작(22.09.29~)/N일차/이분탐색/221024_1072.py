"""

 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

"""
import math
X,Y = map(int,input().split())
origin_Z = (Y*100)//X
min_val = 0
max_val = int(1e100)
save_val = 0
while min_val <= max_val :

    mid_val = (max_val+min_val)//2
    Z = ((Y+mid_val)*100)//(X+mid_val)

    if Z > origin_Z :
        max_val = mid_val-1
        if Z-origin_Z >= 1 :
            save_val = mid_val
    else :
        min_val = mid_val+1
    print(min_val,mid_val,max_val,Z,origin_Z)

if save_val == 0 :
    print(-1)
else :
    print(save_val)
print(29/50*100)