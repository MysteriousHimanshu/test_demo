from collections import defaultdict 


class Graph:
    
    def __init__(self):
        self. grid = [] # defaultdict(list)
        self. parent = defaultdict(lambda : -1)
        
        self. count = 0  
     

        for i in range(int(input())):
            self. grid.append(list(map(int, input().split() )))
            
 
    
    
        
    def find(self, x):
        
        if self.parent[x] == -1:
            return x 
        return self. find( self. parent[x])
        
    
    def union(self, x, y):
        
        x_set = self. find(x)
        y_set = self. find(y) 
        if x_set == y_set:
            return 
        # self. parent[y_set] = x_set
        self. parent[x_set] = y_set
        # self.parent[self. find(x)] = self. find(y) 
        
        self. count -= 1  
    def numIslands(self):
        
        if  len ( self.grid ) == 0:
            return 0 
            
        row = len(self. grid)
        col = len(self. grid[0])
        
        self. count = sum( self. grid[i][j] == 1 for i in range(row) for j in range(col) )
    
        print("count = ", self. count)
        
        for i in range(0, row):
            for j in range(0, col):
                
                
                if self.grid[i][j] == 0:
                    continue 
                
                
                index = i * col + j  
                if j + 1 < col and self. grid[i][j + 1] == 1:
                    
                    self. union(index, index + 1) 
                    
                if i + 1 < row  and self. grid[i + 1][j] == 1:
                    self. union(index, index + col) 
                
        return self. count
    
   
    
def main():
    
    g = Graph() 
    result = g. numIslands() 
    print(result)


if __name__ == '__main__':
    main()
    

'''
File: https://leetcode.com/problems/number-of-islands/discuss/479692/Intuitive-Disjoint-Set-Union-Find-in-JavaPython3
Author: leetcode 200 
Description: Union Find 
'''    
        
        
        
        
        
        
        
        
        
        