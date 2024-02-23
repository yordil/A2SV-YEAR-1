class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        rightlarge = float("-inf")


        for i in range(len(nums)-1 , -1 , -1):
            if rightlarge > nums[i]:
                return True

            while stack and stack[-1] < nums[i]:
                rightlarge = max(stack.pop() , rightlarge)
            stack.append(nums[i])
        
        return False

            

            

