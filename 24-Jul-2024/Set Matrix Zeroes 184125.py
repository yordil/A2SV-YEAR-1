# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rowSet  = set()
        colSet  = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)

        for i in range(len(matrix)):
            if i in rowSet:  
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for i in range(len(matrix[0])):
            if i in colSet:  
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        return matrix

        

        #             matrix[i][0] = "r"
                
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "r":
        #             for k in range(len(matrix[0])):
        #                 if matrix[i][k] != "c":
        #                     matrix[i][k] = 0
                    
        #             break
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "c":
        #             print("///////")
        #             k = i
        #             for k in range(len(matrix)):
        #                 print(matrix[i][j] , (i , j))
        #                 matrix[i][j] = 0

        # print(matrix)
                    
               
                              

        # return matrix

