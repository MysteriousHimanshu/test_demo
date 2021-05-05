'''
File: Mejority Element II  > (N  // 3 )
Author: Leetcode
Description: 
'''
arr = [10, 10, 20, 30, 10, 10]
n = len(arr) 
def logic():
    count1 = 0 
    count2 = 0 
    
    first = 10000
    second = 10000 
    
    for value in arr:
        if first == value:
            count1 += 1 
        
        elif second == value:
            count2 += 1 
        
        elif count1 == 0:
            count1 = 1 
            first = value 
        
        elif count2 == 0:
        
            count2 = 1 
            second = value 
        
        else:
            count1 -= 1 
            count2 -= 1

    
    #we have got 2 majority elements in First and Second variables 
    
    count1 = 0 
    count2 = 0 
    for value in arr:
        if value == first:
            count1 += 1  
        
        elif value == second:
            count2 += 1  
    
    if count1 > n // 3:
        return first 
    if count2 > n // 3 : 
        return second
    
    return -1 
    




x  = logic()
print(x) 