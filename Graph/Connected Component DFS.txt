from collections  import defaultdict 

class Graph:
    
    def __init__(self):
        
        self. graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self. graph[u] .append(v)
        #for undirected 
        self. graph[v].append(u) 
        
    def dfs(self, u, visited, temp = []):
        
        visited[u] = True 
        temp.append(u)
        
        # print(u, end = " ")
        for v in self. graph[u].copy():
            if visited[v] == False:
                temp = self. dfs(v, visited, temp)
        return temp 
        
    def callDFS(self):
        visited = defaultdict(bool) 
        connected_component = [] 
        
        for u in self.graph.copy():
            
            for v in self.graph[u].copy():
                
                if visited[v] == False:
                    temp = self. dfs(v, visited, temp = [] )
                    connected_component .append(temp) 
                    # print()
        print("connected_component = ", connected_component)
def main():
    
    g = Graph()
    for i in range(int(input())): #vertices 
        u, v = map(int, input().split())
        g.addEdge(u, v) 
    
    # print(getattr(g, 'graph'))
    g. callDFS()    
    
if __name__ == '__main__':
    main()

