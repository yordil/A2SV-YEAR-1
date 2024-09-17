# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxxval , minnval = arrays[0][-1] , arrays[0][0]
        ans  = float("-inf")
      
        for arr in arrays[1:]:
            currmax = arr[-1]
            currmin = arr[0]

            ans = max(ans  , abs(currmax - minnval))
            ans = max(ans , abs(maxxval - currmin))
            
            maxxval = max(maxxval , currmax)
            minnval = min(minnval , currmin)

        return ans 