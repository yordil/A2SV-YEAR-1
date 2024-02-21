class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        answercount = 0
        N = len(nums)-1
        for i , v in enumerate(nums):
            
            validsum  = 0
            left , right = 0 , N - i - 1

            while left < right:
                validsum = nums[left] + nums[right]

                if validsum > nums[N-i]:
                    answercount += right  - left 
                    right-=1
                else:
                    left +=1

        return answercount

