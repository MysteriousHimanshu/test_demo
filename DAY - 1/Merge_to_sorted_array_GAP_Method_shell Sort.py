#Merge Two sorted Array without using any additional data structure 
from math import ceil 

class Solution:
    def __init__(self):
        self. arr1 = list(map(int, input().split()))
        self. arr2 = list(map(int, input().split()))

    def nextgap(self, gap):

        if gap <= 1:
            return 0
        return ceil(gap / 2 )
        #or 
        return gap // 2 + gap % 2  
    

    
    def logic(self):
        A = self.arr1 
        B = self. arr2 
        n = len(A)
        m = len(B) 
        
        gap = self. nextgap(n + m) 
        
        while gap > 0:
            
            i = 0 
            while i + gap < n:
                if A[i] > A[i + gap]:
                    #swap 
                    A[i], A[i + gap] = A[i + gap], A[i] 
                i += 1  
        
            if gap > n: #means crossed 
                j = gap - n 
            else:
                j = 0 
            if gap == 1:
                print(A, "\n", B)
            while i < n and j < m:
                if A[i] > B[j]:
                    A[i], B[j] = B[j], A[i] 
                i += 1 
                j += 1  
            
            #after this we have to take care of arr2 means B 
            # Example  when gap == 1 so se have swaped all adjecent to A array1 
            # but when it comes to B i < n condition fails 
            '''
                A = [2, 27, 38, 43]
                B = [5, 6, 7]
                
                before gap 1 both arrays will look like this 
                A = [3, 5, 6, 27]
                B = [7, 43, 38]
                
                now we have gap = 1 means we have to swap adjecent elements 
                so when i == 3 so we swaped 27 to 7 
                now arrays will be 
                A = [3, 5, 6, 7]
                B = [27, 43, 38]
                
                now we proceed for B array 
                but here we can't swap 43 and 38 
                because our i can't point to 43 
                condition fails 
                
                Solution: WE need to check for j itself....
            '''
            if j < m: 
                j = 0 #comparing elements in the second array 
                
                while j + gap < m:
                    if B[j] > B[j + gap]:
                        B[j], B[j + gap] = B[j + gap], B[j] 
                    j += 1 

            gap = self. nextgap(gap)
            
        print(A, B) 

def main():
    obj = Solution()
    obj. logic()
    
    
if __name__ == '__main__':
    main()

