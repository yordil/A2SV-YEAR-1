class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        l = len(mat)
        Sum = 0
        for i in range(l):
           Sum += mat[i][i]
        var = 0
        for j in range(l-1 , -1 , -1):
            Sum += mat[var][j]
            var+=1
        if l % 2 ==0:
            return Sum
        else:
            middle = l // 2
            return Sum - mat[middle][middle]
