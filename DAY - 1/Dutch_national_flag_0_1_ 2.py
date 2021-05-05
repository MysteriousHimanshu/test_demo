
arr = [0, 1, 2, 0, 1, 2, 0, 0, 0]
n = len(arr)
start = 0 
mid = 0 
end = n - 1

while mid <= end:
    
    if arr[mid] == 0:
        arr[start], arr[mid] = arr[mid], arr[start]
        start += 1 
        mid += 1 
    elif arr[mid] == 1:
        mid += 1 
    else:
        arr[mid], arr[end] = arr[end], arr[mid] 
        end -= 1 
print(arr)
