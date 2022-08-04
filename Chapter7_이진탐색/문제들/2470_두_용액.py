import sys

read =sys.stdin.readline
N = int(input())
val_list = list(map(int,read().split()))
val_list.sort()

start = 0
end = N-1
min_val = 1e12

print(val_list)
answer = []
while (start<end):
    sum_ = val_list[start]+val_list[end]

    if min_val > abs(sum_):
        min_val = abs(sum_)
        answer = [val_list[start],val_list[end]]
    print(val_list[start], val_list[end], sum_, min_val,answer)
    if sum_ < 0:
        start += 1
    else:
        end -=1
print(answer[0],answer[1])