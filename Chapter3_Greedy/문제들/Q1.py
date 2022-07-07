# 그룹 수를 최대로 만들기

N = int(input())

array = list(map(int,input().split()))
array.sort()
# array.reverse()

# 공포도가 최대인 모험가를 찾는게 우선인듯?
'''
6
2 2 1 1 3 1
5
2 3 1 2 2
'''

groups = 0

while array :
    maximum_person = array.pop()
    print(maximum_person,array)
    if maximum_person == 1 :
        groups += 1
        break
    else :
        # 최대 공포도를 가진사람은 꼭 공포도 만큼의 그룹을 가져야하니까 그만큼 사람을 빼자.
        # 최대로 만들려면 공포도가 1인 사람들은 혼자 그룹을 만드는게 제일 좋다.
        for person in range(maximum_person-1):
            array.pop()
        groups += 1

for one_person in array :
    groups += 1

print(groups)