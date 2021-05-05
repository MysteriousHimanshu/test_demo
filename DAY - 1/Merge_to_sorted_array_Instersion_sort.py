#Merge Two sorted Array without using any additional data structure 


'''
File: Merge Two sorted Array
Author: Himanshu Jain   
Description:  😊 
                We will use Insertion sort algorithm
                Which is Amazing and easy..
              😄
              
'''
class Solution:
    
    def __init__(self):
        
            
        self. dataset1 = list(map(int, input().split())) #[1, 2, 3, 7]
        self. dataset2 = list(map(int, input().split())) # [4, 5, 6 ]
        
    
    def logic(self):
    
        
        A = self. dataset1 
        B = self. dataset2 
        
        n = len(A) 
        m = len(B)
        print("Before = ", A, B)
        print("after  = ", end = " ")
                
        for i in range(0, n):
            
            if A[i] > B[0]: #checking first of array2...
                #perform Swap 
                A[i], B[0] = B[0], A[i] 
            
            #rearranging elements in B after Swaping 
            
            j = 0 
            while j  + 1 < m and B[j] >  B[j + 1]:
                B[j], B[j + 1] = B[j + 1], B[j] 
                j += 1 
                
        print(A, B)
def main():
    
    obj = Solution() 
    obj. logic() 
        
        
if __name__ == '__main__':
    main()        

'''
Description: Time = O(N * M) 
             Space = O(1) # constant 

'''
        
        
    