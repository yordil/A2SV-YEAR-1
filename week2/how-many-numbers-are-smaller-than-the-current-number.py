class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortt =  sorted(nums)
        
        ans = []
        
        for n in nums:
            ans.append(bisect_left(sortt , n))
            
        return ans
        
        
        
#         counter = [0] * (max(nums)+1)
#         result =[]
#         for i in range(len(nums)):  
#             counter[nums[i]] +=1      
#         for i in range( 1 , len(counter)):
#             counter[i] += counter[i-1];
#         for i in nums:
#             if i == 0:
#                 result.append(0)
#             else:
#                 result.append(counter[i-1])
#         return result
            
            