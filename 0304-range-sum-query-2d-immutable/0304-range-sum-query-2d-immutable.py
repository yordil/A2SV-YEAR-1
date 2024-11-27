class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.row, self.col = len(self.mat), len(self.mat[0])
        
        self.prefix = [[0] * (self.col + 1) for _ in range(self.row + 1)]
        for i in range(self.row):
            for j in range(self.col):
                self.prefix[i + 1][j + 1] = self.prefix[i + 1][j] + self.mat[i][j]
      
        for i in range(self.col):
            for j in range(self.row):
                self.prefix[j + 1][i + 1] += self.prefix[j][i + 1]
         


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total_region = self.prefix[row2+1][col2+1]
        left_side = self.prefix[row2+1][col1]
        above =  self.prefix[row1][col2+1]
        duplicated_region = self.prefix[row1][col1]


        
        return (total_region - left_side + duplicated_region - above  )
      
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)