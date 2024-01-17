from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.row, self.col = len(self.mat), len(self.mat[0])
        
        self.prefix = [[0] * (self.col + 1) for _ in range(self.row + 1)]
        for i in range(self.row):
            for j in range(self.col):
                self.prefix[i + 1][j + 1] = self.prefix[i + 1][j] + self.mat[i][j]
       
        for j in range(self.col):
            for i in range(self.row):
                self.prefix[i + 1][j + 1] += self.prefix[i][j + 1]

        print(self.prefix)
       


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return (self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1] - self.prefix[row1][col2+1]  )
      
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)