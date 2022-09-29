import sys
read = sys.stdin.readline

# 문자열로 받아들이자.
val = read().split()

# 8진수를 먼저 10진수로 변환하는 작업을 하자.
tens = 0
for idx,v in enumerate(val[0]):
    tens += int(v)*(8**(len(val[0])-idx-1))

# 10진수를 2진수로 변환하자.
from collections import deque
twos = deque()

while tens != 0 :
    twos.appendleft(str(tens % 2))
    tens = tens // 2

# 위에서 2진수는 역방향으로 읽어야한다.
# twos.reverse()
if len(twos) == 0 :
    print(0)
else :
    print(int(''.join(twos)))


num = int(input(),8)
num = bin(num)
print(num[2:])