import sys
read = sys.stdin.readline

N,K = map(int,read().split())
g_x = []
max_x = 0
for _ in range(N):
    g,x = map(int,read().split())
    max_x = max(max_x,x)
    g_x.append([g,x])

ice_array = [0 for _ in range(max_x+1)]

for g,x in g_x :
    ice_array[x]=g

"""
곰이 좌우로 K만큼 떨어져 있는 얼음들을 긁어모을 수 있다.
"""
loc = 0
left = loc - K
if left < 0 :
    left = 0
right = loc + K
now_val = sum(ice_array[left:right+1])
max_val = now_val
while right < max_x:
    # 이제 곰이 한칸 움직이자.
    loc += 1
    # 좌우의 위치도 변화하면서 무게를 추가햇다 뺐다가 하자.
    left = loc - K
    if left <= 0 :
        left = 0
    else : # left는 처음엔 좀 특별하다. left가 1이상일 경우에 left-1의 위치에 있는 것을 빼주기 시작하자.
        now_val -= ice_array[left-1]

    right = loc + K
    now_val += ice_array[right]
    max_val = max(max_val,now_val)

print(max_val)

