import sys
read = sys.stdin.readline

N = int(read())
tips = [0]
for i in range(1,N+1):
    tips.append(int(read()))

tips.sort(reverse=True)

result = 0
for n in range(N):
    temp_tip = tips[n] - ((n+1)-1)
    if temp_tip < 0 :
        temp_tip = 0
    result += temp_tip
print(result)
