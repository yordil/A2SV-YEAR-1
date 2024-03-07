class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag =  False
        m = len(matrix)
        n = len(matrix[0])

        for i in range(len(matrix)):
            if matrix[i][n-1] < target:
                continue
            else:
                left , right  = 0 , n - 1 
                flag  = True
                while left <= right:
                    
                    midd = (left + right) //2
                    
                    if matrix[i][midd] > target:
                        right = midd - 1
                    elif matrix[i][midd] < target:
                        left = midd +  1
                    else:
                        return True

                if flag:
                    break

            return False