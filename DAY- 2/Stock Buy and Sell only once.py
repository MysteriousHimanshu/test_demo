'''
File: Stock and Buy only None
Author: Leetcode 121 
Description: 
        Time -O(N)
        Space constant O(1) 
'''
from sys import maxsize 
arr = [7, 1, 5, 3, 6, 4] 
n = len(arr) 
# output = 5 --->>> buy 1 and sell on 6 output = (6 - 1) = 5 


minprice = maxsize 
maxprofit = 0 

for i in range(0, n):
    
    minprice = min(minprice, arr[i])
    maxprofit = max(maxprofit, arr[i] - minprice)

print(maxprofit)


    