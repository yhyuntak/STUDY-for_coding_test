import sys
read = sys.stdin.readline
N = int(read())
distance = list(map(int,read().split()))
oil = list(map(int,read().split()))

now_oil_cost = oil[0]
total = now_oil_cost * distance[0]

for i in range(1,len(distance)):
    next_oil_cost = oil[i]
    if next_oil_cost < now_oil_cost :
        # 도착한 도시의 기름 값이 현재보다 더 작으면 갱신하자.
        now_oil_cost = next_oil_cost
    # 기름값이 작지 않으면 갱신하지 않고 거리와 곱해지고,
    # 기름값이 작으면 갱신되서 거리와 곱해지고 비용을 더한다.
    total += now_oil_cost*distance[i]

print(total)