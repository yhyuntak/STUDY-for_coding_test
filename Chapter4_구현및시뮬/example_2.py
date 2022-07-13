N = int(input())
count = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if str(3) in str(h)+str(m)+str(s):
                count += 1

print(count)
