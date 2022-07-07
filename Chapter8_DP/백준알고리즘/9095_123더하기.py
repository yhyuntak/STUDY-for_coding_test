#
# def recursive_function(N,count):
#     for i in range(1,4):
#         if N-i > 0 :
#             count = recursive_function(N-i,count)
#         else :
#             # N이 1이면 단말 노드를 만났기 때문에 count를 하나 올리고 return
#             count += 1
#             return count
#     return count
#
# T = int(input())
#
# input_array = []
# for j in range(T):
#     input_array.append(int(input()))
#
# for k in range(T):
#     count = 0
#     count = recursive_function(input_array[k],count)
#     print(count)

T = int(input())
input_array = []
for _ in range(T):
    input_array.append(int(input()))

'''
이게 무조건 bottomup 방식으로 푼다고 생각해야하는 듯.
딱 유형은 지금까진 2개다. 최소같은 단어가 나오면 원래 하던 유형이고,
뭔가 모든 경우를 구하는 것은 타일문제를 생각하자. 
'''

d = [0]*(11)
d[1] = 1
d[2] = 2
d[3] = 4


for i in range(4,max(input_array)+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]

for j in input_array:
    print(d[j])