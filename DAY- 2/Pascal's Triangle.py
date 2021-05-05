def pascalTriangle(n):
    
    
    answer = [ [] for i in range(n)] 
    
    for i in range(n):
        for j in range(0, i + 1):
            
            if j == 0 or j == i:
                answer[i].append(1)
            else:
                answer[i].append(answer[i - 1][j - 1] + answer[i - 1][j])
                # answer.append([1]
    # print(answer)
    for i in answer:
        print(i) 
    
pascalTriangle(6)