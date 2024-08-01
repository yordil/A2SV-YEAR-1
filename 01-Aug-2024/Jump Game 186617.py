# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = 0
        for i in range(len(nums)):
            if maxx < i:
                return False
            maxx = max(maxx, i + nums[i])
        return True
