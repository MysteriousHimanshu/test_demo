'''
File: count inversion
Author: GFG ..... Merge sort
Description: Time -(NlogN)
        Space = O(N)
'''

def countInversion(arr, n): # Time - N ^ 2 
    inversion_count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            
            if arr[i] > arr[j]:
                inversion_count += 1 
    
    print(inversion_count)
count = 0  
def mergeSort(arr):
        global count 
        if len(arr) <= 1:
            return 

            
        mid = len(arr) // 2 
        
        A =  arr[:mid] 
        B = arr[mid: ]
        
        mergeSort(A)
        mergeSort(B) 
        
        merge(arr, A, B)


def merge(arr, A, B):
    global count 
    
    i = j = k = 0 
    n = len(A) 
    m = len(B) 
    while i < n and j < m:
        
        if A[i] < B[j]:
            
            arr[k] = A[i]
            i += 1 
            k += 1 
        
        else:
            arr[k] = B[j] 
            j += 1 
            k += 1 
            count += (n - i )        
    #checking for i seperatly 
    
    while i < n:
        arr[k] = A[i] 
        k += 1 
        i += 1 
    while j < m:
        arr[k] = B[j] 
        k += 1 
        j += 1 
        
def main():
    
    arr = [8, 4, 2, 1]
    n = len(arr) 
    # countInversion(arr, n) #quardatic time complexity 
    global count 
    mergeSort(arr)
    print(arr)
    print(count)
    


if __name__ == '__main__':
    main()        




def Description():
    '''
    Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
    Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
    Example: 
    
    Input: arr[] = {8, 4, 2, 1}
    Output: 6
    
    Explanation: Given array has six inversions:
    (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
    
    
    Input: arr[] = {3, 1, 2}
    Output: 2
    
    Explanation: Given array has two inversions:
    (3, 1), (3, 2)         
    '''
