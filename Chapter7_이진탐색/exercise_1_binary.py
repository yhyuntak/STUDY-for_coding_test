def binary_search(array,start,target,end):
    if start > end :
        return "no"

    mid = (start+end)//2

    if array[mid] == target :
        return "yes"
    elif array[mid] > target:
        return binary_search(array, start, target, mid - 1)
    elif array[mid] < target:
        return binary_search(array, mid+1, target, end)


n = int(input())
receive_array = list(map(int,input().split()))
receive_array.sort()
m = int(input())
ask_array = list(map(int,input().split()))

for target in ask_array:
    answer = binary_search(receive_array,0,target,n-1)
    print(answer,end=' ')