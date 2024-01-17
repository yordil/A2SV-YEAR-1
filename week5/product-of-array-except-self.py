class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = [1] * len(nums)
        prefix=1
        
        for i in range(len(nums)):
            num[i] *=prefix
            prefix *=nums[i]
        print(num)
        postfix=1
        
        for i in range(len(nums)-1 , -1 , -1):
            num[i] *=postfix
            postfix *=nums[i]
            
        return num
            