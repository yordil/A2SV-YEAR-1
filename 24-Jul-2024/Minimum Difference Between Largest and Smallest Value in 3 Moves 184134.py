# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        answer = 0

        if len(nums) <= 4:
            return 0
        else:
            nums.sort()
            a = nums[-1] - nums[3]
            a = min(a , nums[-4] - nums[0])
            a = min( a , nums[-3] - nums[1])
            a  = min(a  , nums[-2] - nums[2])

            answer = a
        return answer


            

        return 1