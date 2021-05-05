from collections import defaultdict 

class Graph:
    
    
    def __init__(self):
        
        self. graph = defaultdict(list) 
    
    def addEdge(self, u, v, w ):
        
        self. graph[u].append([v, w]) 
        self. graph[v].append([u, w])
        
    def minimum_distance(self, distance, visited):
        
        maximum = 10 ** 5 
        min_path_node = None 
        for node, weight in distance.items():
            
            if visited[node] == False and weight < maximum:
                maximum = weight 
                min_path_node  = node
        
        return min_path_node
        
    
    def dijkstra_Algo(self, src):
        
        visited = defaultdict(bool) 
        
        distance = defaultdict(lambda : 10** 5) 
        
        
        distance[src] = 0 
        for edges in  self. graph.copy():
            
            u = self. minimum_distance(distance, visited) 
            
            visited[u] = True 
            
            for v, w in self. graph[u].copy():
                
                if visited[v] == False and distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w 
        print(distance)
                
        

def main():
    
    g = Graph() 
    vertices = int(input())
    for i in range(vertices):
        u, v, w = map(int, input().split() )
        g.addEdge(u, v, w)
    g. dijkstra_Algo(1)
        
        
        
        
if __name__ == '__main__':
    main()        
        
        
        
        
        
        
        
        
        
        