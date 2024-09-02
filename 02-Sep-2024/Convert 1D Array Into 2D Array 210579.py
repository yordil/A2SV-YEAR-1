# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr =[]
        temparr = []
        if m*n != len(original):
            return []
        
        else:
            idx = 0
            for i in range(m):
                temparr = []
                for j in range(n):
                    temparr.append(original[idx])  
                    idx+=1
                arr.append(temparr)   
        return arr
                    