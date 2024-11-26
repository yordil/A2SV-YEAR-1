class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()

        answer  = []

        for idx , num in enumerate(nums):

            if idx > 0 and nums[idx] == nums[idx -1]:
                continue
            
            l , r  = idx +  1 , len(nums)  - 1

            while l < r:

                targetSum = nums[idx] + nums[l] + nums[r]

                if targetSum > 0:
                    r-=1
                elif targetSum < 0:
                    l+=1
                else:
                    answer.append([nums[idx] , nums[l] , nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                
        return answer
                    



