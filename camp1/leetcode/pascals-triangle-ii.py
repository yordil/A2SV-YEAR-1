class Solution:
    def getRow(self, r: int) -> List[int]:
        
        if r == 0:
            return [1]
        if r == 1:
            return [1, 1]
        prev = self.getRow(r -1)
        curr = [1] * (r + 1)

        for i in range(1 , r):
            curr[i] = prev[i] + prev[i-1]
        
        return curr