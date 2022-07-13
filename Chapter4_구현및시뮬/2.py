import time
input_ = input()

since = time.time()
row = int(input_[1])
col = int(ord(input_[0]) - ord('a') + 1)
case_1 = [[1,2],[1,-2],[-1,2],[-1,-2]]
case_2 = [[2,1],[2,-1],[-2,1],[-2,-1]]

results = 0

for _1 in case_1 :
    temp = [row+_1[0],col+_1[1]]
    if temp[0]*temp[1] >= 1 and temp[0] < 9 and temp[1] < 9  :
        results += 1
for _2 in case_2 :
    temp = [row+_2[0],col+_2[1]]
    if temp[0]*temp[1] >= 1 and temp[0] < 9 and temp[1] < 9  :
        results += 1
print("time : {0:.4f}".format(time.time()-since))
print(results)