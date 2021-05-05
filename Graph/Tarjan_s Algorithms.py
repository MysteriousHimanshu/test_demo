from collections import defaultdict 

'''
    File: Tarjen's Algorithms
        Author: GFG 
    Description: one traversal with O(V + E) 
'''

class Graph:
    
    def __init__(self):
        
        self. graph = defaultdict(list) 
        self. dis = defaultdict(lambda : -1)
        self. low = defaultdict(lambda : -1)
        self. time = 0 
        
    def addEdge(self, u, v):
    
        self. graph[u].append(v)
 
    def tarjan_algo(self):
        
        isInStack = defaultdict(bool) 
        stack = [] 

        for u in self.graph.copy():
            for v in self. graph[u].copy():
                
                if self. dis[v] == -1:
                    self. dfs(v, isInStack, stack )
        
    def dfs(self, u, isInStack, stack):
        
        stack.append(u) 
        isInStack[u] = True 
        # print(u, end = " ")
        self. dis[u] = self. time 
        self. low[u] = self. time 
        self. time += 1 
        
        for v in self. graph[u].copy() :
            
            if self. dis[v] == -1:
                
                self. dfs(v, isInStack, stack) 
                self. low[u] = min(self. low[u], self. low[v])
            
            elif isInStack[v] == True: #back Edge 
            
                self. low[u] = min(self. low[u], self. dis[v])
        
        if self.low[u] == self. dis[u]: #head node 
            top = -1
            while top != u: 
                top = stack.pop() 
                print(top, end  = " ")
                isInStack[top] = False 
            print() 
            
            
                
    
def main():
    
    g = Graph()
    for i in range(int(input())):
        u, v = map(int, input().split() )
        g. addEdge(u, v) 

    g. tarjan_algo() 
    


if __name__ == '__main__':
    main()
