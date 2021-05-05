#Find duplicates in array 
'''
File: Slow and Fast ... Floyd's cycle detection 2 pointer, hare and Tortoise 
Author: Leetcode Find the duplicate Number      #287 

Description: T - O(N) 
             S - O(1)
'''
arr = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]

def isCycle():

    slow = fast = 0

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if  slow == fast:
            fast = 0 
            while slow != fast:
                fast = arr[fast] 
                slow = arr[slow] 
                # print(slow, fast)
            return fast 

x = isCycle()
print(x)
