'''
File: Permutation Sequence find Kth Permutation 
Author: Leetcode 60 Hard 
Description: 
'''

arr = [1, 2, 3]
k = 3

def next_permutation(arr, n):
    
    i = n - 1 
    
    while i != 0:
        
        if arr[i] > arr[i - 1]:
            break 
        else: 
            i -= 1 
    
    i -= 1 #setting arr[i - 1] 
    if i >= 0:
        j = n - 1 
        while arr[j] < arr[i]:
            j -= 1 
        arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr 

def method1():
    for i in range(1, k):
        arr = next_permutation(arr, len(arr))
    print(  "".join(map(str, arr) ) ) 
    
def method2():
    global k 
    ans = ''
    fact = 2 
    k -= 1 
    while k : 
        i, k = divmod(k, fact)
        ans += str(arr.pop(i)) 
        fact //= len(arr) 
    
    ans += ''.join(map(str, arr) ) 
    print(ans)
    
help(divmod)    
method2()
        
        
