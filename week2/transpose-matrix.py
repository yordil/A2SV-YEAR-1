class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row  = len(matrix)
        col = len(matrix[0])
        newmatrix = []
        for i in range(col):
            temparr = []
            for j in range(row):
                temparr.append(matrix[j][i])
                
            newmatrix.append(temparr)
            
        return newmatrix