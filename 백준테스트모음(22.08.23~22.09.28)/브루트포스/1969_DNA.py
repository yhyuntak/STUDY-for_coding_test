#220915

"""
각 글자의 앞만 따서 DNA만들고
해밍거리는 같은 위치의 글자가 다른 것을 세는 것

이 거리들의 합이 가장 작을 DNA를 만들어야되는거구나
그럼 모든 DNA들을 보고 각 위치에 가장 많은 뉴클레오티드를 선택하면됨.
최대 개수가 똑같은게 있을 경우 그것들도 추가해서 나중에 사전순으로 배열

"""

N,M = map(int,input().split())

DNA_array = []
for _ in range(N):
    DNA_array.append(input())

temp_dict = {0:'A',1:'C',2:'G',3:'T'}
temp_dict2 = {'A':0,'C':1,'G':2,'T':3}

save_array = ['' for _ in range(M)]
save_max = [0 for _ in range(M)]
for m in range(M):
    temp_array = [0,0,0,0]
    for n in range(N):
        DNA = DNA_array[n][m]
        temp_array[temp_dict2[DNA]] += 1
    max_val = max(temp_array)
    save_max[m] = max_val
    for i in range(4):
        if temp_array[i] == max_val and save_array[m] == '':
            save_array[m] =temp_dict[i]

print(''.join(save_array))
print(N*M - sum(save_max))