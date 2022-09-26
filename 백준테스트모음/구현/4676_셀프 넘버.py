"""
d(n)을 n과 n의 각자리수를 더한 함수이다.

생성자가 없는 숫자를 셀프 넘버라고 한다.
n으로 d(n)을 못만드는것.
"""


# 1부터 시작해서 10000까지 생성자를 만들어보고 해당 수를 삭제하는 느낌으로

array = [[1] for _ in range(10001)]

for j in range(1,10001):
    temp = j
    for k in str(j):
        temp += int(k)

    if temp < 10001 :
        array[temp] = 0

for i,m in enumerate(range(1,10001)):
    if array[m] != 0 :
        print(i+1)