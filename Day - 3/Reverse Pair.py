def bstSolution():
    
    class Node:
        
        def __init__(self, val):
            
            self. data = val 
            self. left = None 
            self. right = None 
            self. count_greater = 1 
    
    def insert(root, data):
        
        if root is None:
            return Node(data)
        if root. data > data: 
            root.left = insert(root.left, data) 
        else:
            root. count_greater += 1 
            root. right = insert(root. right, data)
        
        return root 
        
    # def search(root)
        
        
    def search(root, key):
        
        if root is None:
            return 0
        if root. data == key:
            # return root.data 
            return root. count_greater 
        if key > root.data:
            return search(root. right, key) 
            
        return root. count_greater + search(root. left, key) 
    
    
    def inorder(root):
        if root is None:
            return 
    
        inorder(root. left)
        print(root.data, end = "  ")
        inorder(root. right)
    
    def bfs(root):
        if root is None:
            return 
        
        queue = [root] 
        # print(root.data)
        while queue : 
            front = queue.pop(0) 
            print(front. data, end = ", ")
            if front.right: queue.append(front.right) 
            if front.left: queue.append(front.left)
            
    answer = 0 
    for i in arr:
        answer += search(root, 2 * i + 1) #return all elements greater then this 
        root = insert(root, i) 
        
answer = 0 
def merge(A, B):
    global answer
    i = j = 0 
    m = len(A) 
    n  = len(B) 
    
    while i < m and j < n: 
        if A[i] <= 2 * B[j]:
             i += 1
        else:
            
            answer += len(A) - i 
            j += 1 
    return sorted(A + B) 

def mergeSort(arr):
    if len(arr) <= 1 : 
        return arr 
    mid = len(arr) >>  1 # divide by 2  
    left = mergeSort(arr[0: mid])
    right = mergeSort(arr[mid: ])

    return merge(left, right)

def main(): 
    from typing import List
    help(List)
    arr = [1, 3, 1, 3, 2]
    n = len(arr) 
    # help(List)    
    mergeSort(arr) 
    print(answer)
    print(arr)

main()
    
    
    
    
    
    
    