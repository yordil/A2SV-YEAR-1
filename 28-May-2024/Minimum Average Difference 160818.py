# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        lenn = len(nums)

        prefixsum = [0] + list(accumulate(nums))
        
        minn = float("inf")
      
        ans = 0 
        for i in range(len(nums)-1):

            lefthalf = prefixsum[i+1] // (i+1)
            righthalf = (prefixsum[-1]  - prefixsum[i+1]) // (lenn - (i+1))
            print(lefthalf , righthalf , abs(righthalf  - lefthalf))
            if minn > abs(righthalf  - lefthalf):
                ans = i
                minn = min(minn , abs(righthalf  - lefthalf))

        return ans if sum(nums) / lenn >= minn else lenn-1