
# Kadane's Algorithm 
'''
File: Kadane's Algo 
Author: GFG
Description: Time - O(N)
             Space - O(1)
'''
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

maximum = 0 
curr = 0 
for i in arr:   
    curr += i 
    curr = max(curr, 0)
    maximum = max(maximum, curr)

print(maximum)