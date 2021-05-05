
'''
File: SET matrix zeroes
Author: leetcode 73
Description:  
time = O(N ^ 2) 
sapce - O(1) 
wow 
'''
 
matrix = [[1,1,1],[1,0,1],[1,1,1]]
 
def logic():
    
            row = len(matrix)
            col = len(matrix[0])

            row_flag = False 
            col_flag = False 

            for i in range(0, row):
                for j in range(0, col):
                    if i == 0 and  matrix[i][j] == 0:
                        row_flag = True 
                    if j == 0 and matrix[i][j] == 0:
                        col_flag = True 
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0  #row
                        matrix[0][j] = 0  #column 

            for i in range(1, row):
                for j in range(1, col):

                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0 

            if row_flag: #set all columns 
                for j in range(0, col):

                    matrix[0][j] = 0 
            if col_flag:
                for i in range(0, row):
                    matrix[i][0] = 0 

logic()