N = input()
cycle = 0

original_N = N

while True :


    if len(N) < 2 : N = '0'+N
    temp_sum = str(int(N[0]) + int(N[1]))
    new_num = N[-1] + temp_sum[-1]
    N = new_num
    cycle+=1
    if int(original_N) == int(N):  break

print(cycle)