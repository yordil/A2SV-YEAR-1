class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()

        boat = 0
    
        left , right = 0 , len(p) -1

        while left <= right:
            if left == right:
                boat+=1
                break
            if p[left] + p[right] <= limit:
                boat +=1
                left+=1
                right-=1
            elif p[left] + p[right] > limit:
                boat +=1
                right -=1
        return boat