from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        longestWindow = 0
        start = 0

        for i in range(len(nums)):
            zeroCount += 1 if nums[i] == 0 else 0

            while zeroCount > 1:
                zeroCount -= 1 if nums[start] == 0 else 0
                start += 1

            longestWindow = max(longestWindow, i - start)

        return longestWindow

