class Solution:
    def uniquePathsIII(self, arr: List[List[int]]) -> int:
        
          
        self.ans = 0 
        m =  len(arr)
        n = len(arr[0])
        start = end = 0 
        moves_without_obstacles = 0 
        # @cache
        def dfs(i, j, remaining_mvs):
            
            if  i < 0 or i >= m or j < 0 or j >= n or arr[i][j] == -1:
                return 
            if arr[i][j] == 2  and remaining_mvs == 0:
                self.ans += 1 
                print("himanshu Jain ", i, j)
                return 
            
            save = arr[i][j]
            arr[i][j] = -1                 #mark visited 
            
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(x, y, remaining_mvs - 1) 
            
            arr[i][j] = save  #most Important to set it. 
            
        #we know there is only one start and one end.1 & 2 
        for i in range(0, m):
            for j in range(0, n):
                if arr[i][j] == 1:
                    start, end = i, j 
                    
                if arr[i][j] != -1:
                    
                    moves_without_obstacles += 1 
                
        
        print(start, end, moves_without_obstacles)
        dfs(start, end, moves_without_obstacles - 1)
        
        return self. ans 
                
        