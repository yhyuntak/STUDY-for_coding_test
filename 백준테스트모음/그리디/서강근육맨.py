"""
되도록 pt 한번에 기구 2개 사용
그리고 다 한번씩만 사용할 것임

pt 한번 받을 때의 근손실 정도가 M을 넘지 않도록 하고 싶다.
M의 최소값은?

근손실 정도는 t의 합임.

"""
import sys
input = sys.stdin.readline
N = int(input())
loss_list = list(map(int,input().split()))
loss_list.sort()
# 운동기구가 홀수개이면 제일 무거운 것을 마지막 날에 들면 되고 이게 최대가 될듯
if len(loss_list) % 2 == 1 :
    temp = len(loss_list)//2
    i = 0
    max_val = loss_list[-1]
    while i != temp :
        max_val = max(max_val,loss_list[i]+loss_list[-2-i])
        i+=1
    print(max_val)

# 운동기구가 짝수개이면, 제일 가벼운 것과 제일 무거운걸 드는 날이 가장 최대가 될듯
else :
    temp = len(loss_list)//2
    i = 0
    max_val = 0
    while i != temp+1 :
        max_val = max(max_val,loss_list[i]+loss_list[-1-i])
        i+=1
    print(max_val)
