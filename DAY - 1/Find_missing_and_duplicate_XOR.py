from math import log #needed to find position of set bit 

arr = [ 4, 3, 6, 5, 2, 4  ]
n = len(arr)


def logic():
    xor = 0 
    for i in arr: #xor of all array elements 
        xor ^= i 

    for i in range(1, n + 1): #xor of 1 to n so that duplicate will nullify
        xor ^= i  

    x = y = 0   #bucket1 , #bucket2  
    
    k = log(xor, 2) #it will give position to  last set bit 
    msb = 1 << int(k) # it will give us most significant bit 
    
    for i in arr: #isolating missing and repeating number 
        if i & msb:
            x ^= i 
        else:
            y ^= i  
    
    for i in range(1, n + 1): # now nullify duplicates 
        if i & msb:
            x ^= i  
        else: 
            y ^= i 
    print(x, y) #printing answer 

logic()
            
            
            
            
    
