class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dict = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i , j) not in dict:
                    matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                    dict[(i,j)] = 1
                    dict[(j , i)] = 1
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        
            
        
        
        
        
        
        
#         newmatrix = []
#         col = len(matrix)
#         for i in range(col):
#             temparr = []
#             for j in range(col):
#                 temparr.append(matrix[j][i])

#             newmatrix.append(temparr)
#         for i in range(col):
#             newmatrix[i] = newmatrix[i][::-1]
            
       
        
        

       

                