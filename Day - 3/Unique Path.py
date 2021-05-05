
arr = [[0 for i in range(7)] for i in range(3) ]
from functools import lru_cache 

def memoization():
    
    @lur_cache 
    def recursion(i, j, answer = 0  ):
        if  i == 0  and j == 0:
            return 1 
        if i < 0 or j < 0:
            return 0 
    
        return recursion(i, j - 1, answer) + recursion(i - 1, j, answer) 
        
    x = recursion(2, 6)
    print(x)
    
def math():
    
    '''
    File: Leetcode 
    Author:Texasorh  https://leetcode.com/problems/unique-paths/discuss/501214/Python-simple-math-calculation.-clean-code
    Description: 
        Space - O(1)
        T = O(N) 
        Wow 
    '''
    
    #school Math 
    # N_C_ R = n ! // R! - (N - R) ! 
    from math import factorial 
    
    row = 5
    col = 7 
    
    right = row - 1 
    down = col - 1 
    
    x = factorial(right + down) // factorial(right) // factorial(down)
    print(x) 
    
    

math() 
    
    
    
