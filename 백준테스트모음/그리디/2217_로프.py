#220915

"""

각 로프마다 들수 있는 무게가있고
로프들을 병렬로 연결하면 W/K만큼 무게가 걸림.

로프들을 이용해서 최대로 들수 있는 중량은?

"""
import sys
read = sys.stdin.readline
N=int(read())
rope_weight = []
for _ in range(N):
    rope_weight.append(int(read()))

# 음. W/K를 허용무게가 가장 낮은거부터 빼면서 확인해봐야할듯
# W/K > min(rope_weight) 여야 들 수 있는 W가 정해지는 것이니, W > min(rope_weight)*K 를 생각.
rope_weight.sort()
weight_array = []

for K in range(N,0,-1):
    min_rope = rope_weight.pop(0)
    weight_array.append(min_rope*K)

print(max(weight_array))