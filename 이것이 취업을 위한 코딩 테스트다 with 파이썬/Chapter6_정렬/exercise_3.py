n,k = map(int,input().split())

total_array = []
for i in range(2):
    total_array.append(list(map(int,input().split())))
array_A = total_array[0]
array_B = total_array[1]

def count_sort(array):
    if len(array) <= 1 :
        return  array

    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return count_sort(left_side)+[pivot]+count_sort(right_side)

sorted_array_A = count_sort(array_A)
sorted_array_B = count_sort(array_B)
sorted_array_B.reverse()

print(sorted_array_A)

for i in range(k):
    if sorted_array_A[i] < sorted_array_B[i] :
        sorted_array_A[i] = sorted_array_B[i]
    else :
        break
print(sorted_array_A)
print(sum(sorted_array_A))