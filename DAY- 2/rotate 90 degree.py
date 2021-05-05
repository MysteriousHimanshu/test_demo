matrix = [ [1, 2], [4, 5], [3, 6]]
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 

for value in matrix:
    print(value)

row = len(matrix)
col = len(matrix[0])

matrix = [  [ matrix[i][j] for i in range(row) ] for j  in range(col) ] 



# matrix  = [ value[::-1] for value in matrix]
for i in range(row):
    matrix[i] = matrix[i][::-1]
    



print() 
for value in matrix:
    print(value) 

# print() 

# for value in matrix:
#     print(value[::-1])