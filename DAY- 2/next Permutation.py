'''
File: Next Permutaion
Author: leetcode 31 
Description: time - > O(N)
            Space - > O(1) constant 
'''
def nextPermutation(arr, n):
        i = n - 1
        while i > 0:
            
            if arr[i] > arr[i - 1]: # we can perfrom swap 
                break 
            else:
                i -= 1 
        
        i -= 1 #for pointing the previous number arr[i - 1] 
        if i >= 0:
            j = n - 1  #finding max then arr[i] 
            
            while j >  i : 
                if arr[j] > arr[i]: 
                    break 
                else:
                    j -= 1 
            
            #swap 
            arr[i], arr[j] = arr[j], arr[i]
        reverse(arr, i + 1, n - 1)
        
        print(arr)

def reverse(arr, start, end):
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start] 
        start += 1 
        end -= 1 







arr = [3, 2, 1]

n = len(arr)        
nextPermutation(arr, n)
print(arr)
