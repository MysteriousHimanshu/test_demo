
'''
File: search in 2d matrix   
Author: Leetcode 74 
Description:  Time - O(N)  # binary Search 
        space = O(1)
'''

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def logic(): 
            n = len(arr)
            m = len(arr[0])
            row = 0 
            col = m - 1 

            while n > row >= 0 and m > col >= 0 : 

                if arr[row][col] == target:
                    return True 
                elif arr[row][col] < target:
                    row += 1 

                else:
                    col -= 1
            return False

print(logic())