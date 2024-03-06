class Solution:
    def mySqrt(self, x: int) -> int:
        
        l , r = 0 , x
        ans =  float("inf")
        while l <= r:

            midd = (l + r) // 2 
            if midd ** 2 > x:
                r = midd - 1
            elif midd**2 < x:
                l = midd + 1
                ans = min(midd , x)

            else:
                return int(midd)
        return ans