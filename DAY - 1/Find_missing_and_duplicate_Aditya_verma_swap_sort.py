'''
File: Missing and duplicate
Author: Aditya verma Youtube 
Description: this approach is using a SWAP sort Algorithm to do this in linear time.

'''
arr = [1, 2, 4, 3,  1]
n = len(arr)


i = 0 
while i < n :
    
    temp = arr[i]
     
    if temp != arr[temp - 1]:
        #swap 
        arr[i], arr[temp - 1] = arr[temp - 1], arr[i] 
    else:
        i += 1 
for i in range(0, n, 1):
    if arr[i] != i + 1 :
        print("Missing = ", i + 1)
        print("duplicate = ", arr[i])
        
''' Time = O(N)
    Space = O(1) 
''' 
