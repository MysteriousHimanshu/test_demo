# from deque import que
from collections import defaultdict, deque 

class Graph:
    
    def __init__(self):
        #initializing garph  -->>> as Adjacency list 
        self. graph = defaultdict(list) 
    
    def addEdge(self, u, v):
        #For directed Graph 
        self. graph[u].append(v)
        #For Undirected 
        self. graph[v].append(u) 

        
    def dfs(self, v, visited):
        visited[v] = True 
        print(v, end = " ")
        for x in self. graph[v].copy() :
            if visited[x] == False:
                self. dfs(x, visited) 
    
    def callDFS(self, v ):
        # Graph may contains Cycle so we need to take care 
        #we are visiting each node exactly once 
        
        # for that we use boolean Visited dictionary. 
        
        visited = defaultdict(bool) 
        
        self. dfs(v , visited) 
        
        # this is for Without Parameter 
        
        # for u in self. graph.copy(): 
        #     for v in self.graph[u].copy():
        #         if visited[v] == False:
        #             self. dfs(v, visited)
                
    def bfs(self, u):
        
        visited = defaultdict(bool)
        queue = [] 
        queue.append(u) 
        visited[u] = True 
        
        while queue: 
            
            u = queue.pop(0) 
            print(u, end = " ")
            
            for v in self. graph[u].copy():
                
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True       
                    
    def isCycle(self):
        
        visited = defaultdict(bool) 
        recStack = defaultdict(bool)
        answer = False 
        
        for u  in self. graph.copy():
            for v in self. graph[u].copy():
                    
                if visited[v] == False:
                    answer |= self. dfscycle(v, visited, recStack)
                    # answer |= self. bfsCycle(v, visited) 
        # print()
        print(answer)
    
    def bfsCycle(self, u, visited):
        queue = deque() 
        visited[u] = True 
        queue.append(u) 
        
        while queue: 
            
            u = queue.pop() #not pop(0) Here we are using queue not list 
            
            for v in self. graph[u].copy():
                
                if visited[v] == False:
                    visited[v] = True 
                    queue.append(v) 
                else:
                    return True 
        
        return False             
                    
    
        
        # return answer 
    def dfscycle(self, u, visited, recStack):
        
        visited[u] = True 
        recStack[u] = True 
        for v in self. graph[u].copy():
            if visited[v] == False:
                if  self. dfscycle(v, visited, recStack) :
                    return True 
            elif recStack[v] == True:
                return True 
                
        recStack[u] = False 
        return False 
                                
                    
                    
            
        
        
def main():
    
    g = Graph() #making graph Object 
    
    #taking vertices, edges as input 
    V = int(input())
        
    #one way of inuput     
    # edges =[ (1, 2), (2, 3), (3, 4), (1, 3), (2, 4)]
    # for u, v in edges:
    # g. addEdge(u, v) 
    #add (v, e) in graph
    
    #second way of Input 
    for _ in range(V):
        u, v = map(int, input().split()) 
        g.addEdge(u, v) 
        
        
    #In graph we have only 2 types of traversal to print 
    #the content of the Graph 
    # 1.) Depth First Search (DFS) ---> Traverse Depth wise 
    # 2.) Breadth First Search (BFS) --->> Traverse Breadth(Level) wise 
    
    #applying DFS 
    
    # we can call DFS with parameter if we know from which node we have to start 
    #otherwise  Without parameter
    start = 1 #with parameter
    # g. callDFS(start)
    
    #Calling BFS 
    #level Order Traversal 
    # print()
    
    start = 1# it is our choice 
    # g. bfs(start) 
    
    g. isCycle()
    
    
    
    
    

if __name__ == '__main__':
    main()