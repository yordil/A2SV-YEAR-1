class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [ -1] * len(nums)
        nums.extend(nums)

        stack = []
        myhash = {}

        for i in range(len(nums)):

            while stack and nums[stack[-1]] < nums[i]:
                poped = stack.pop()
                myhash[poped % n] = nums[i]

        
            stack.append(i)

        for i in myhash:

            ans[i] = myhash[i]
        return ans