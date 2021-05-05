from collections import defaultdict 


class Graph:
   
    def __init__(self):
        
        self. graph  = defaultdict(list) 
        
    def addEdge(self, u, v):
        
        self. graph[u].append(v)
        #undirected 
        self. graph[v].append(u)
    
    def dfs(self, u, visited):
        
        visited[u] = True 
        print(u, end = " ")        
        for v in self. graph[u]:
            
            if visited[v] == False:
                
                self. dfs(v, visited) 

    def callDFS(self):
        
        visited = defaultdict(bool) 
        for u in self. graph.copy():
            print(u)
            for v in self. graph[u].copy():
                
                if visited[v] == False:
                    self. dfs(v, visited)

def main():
    
    g = Graph() 
    
    # edges = list(map(int, input().split()))
    
    edges = int(input())
    
    for _ in range( edges):
        
        u, v = input().split() 
        g.addEdge(u, v) 

    g.callDFS()
    


# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 5 1


if __name__ == '__main__':
    main()
                
        
        
        
        
    