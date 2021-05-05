#overlap intervals 
#here we are using Graph connected_componect Concept 

from collections import defaultdict 

class Graph:
    def __init__(self, x ):
        
        self. graph = defaultdict(list)
        self. intervals = [ [1, 5], [6, 10], [15, 17], [4, 7], [16, 20] ] # x 
    
    def buildGraph(self): #this method is used to build Graph 

        intervals = self. intervals
        n = len(intervals)
        for i in range(0, n):
            for j in range(i + 1, n):
                if self. overlap(intervals[i], intervals[j]): #checking overlap 
                    # self. addEdge((intervals[i]), (intervals[j]) )
                    
                    self. addEdge( tuple(intervals[i]),  tuple(intervals[j])  )
                
                    #here we are pasing arugument with typecast because without it this will be 
                    #list and a list can't be a key  .. what a joke 
                    
    
    def overlap(self, a, b):
        #[1, 3], [2, 5]
        return a[0] <= b[1] and a[1] >= b[0] 
    
    def DFS(self, u, visited, connected_compo):
        
            visited[u] = True 
            # print(u)
            connected_compo.append(u)
            for v in self. graph[u]:
                if visited[v] == False:
                    self. DFS(v, visited, connected_compo) 
            return connected_compo
    
    def callDFS(self):
        intervals = self. intervals 
        
        visited = defaultdict(bool)

        res = [] 
        for value in intervals:
                u = tuple(value)
                if visited[u] == False:
                    connected_compo = self. DFS(u, visited, []) 
                    res.append( self. mergeNodes(connected_compo) ) 
                 
        print(res)
    
    def addEdge(self, u, v):
        #undirected 
        self. graph[u].append(v)
        self. graph[v].append(u) 
    
    def mergeNodes(self, nodes):
        #nodes = [[1, 5], [2, 7], [3, 10] ] 
        min_start = min(x[0] for x in nodes) # 1 
        max_end = max(x[1] for x in nodes) # 10 
    
        return [min_start, max_end] # [1, 10]

def main():
    g = Graph()
    g. buildGraph()
    g. callDFS()
if __name__ == '__main__':
    main()                

#time Complexity = quardatic 
# O(N^2) 
'''
building a graph = O(V + E) = (V) + O(E)
in worst case all intervals will mutually overlap so it will O(N^2) 

'''


