class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
       
        left = 0
        Sum = sum(nums[:k])
        maxavg = Sum/k 
        for i in range(k , n):
            Sum += -nums[left] + nums[i]
            maxavg = max(maxavg , Sum/k)

            left +=1
               
                
        return maxavg
                
        
# #         class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
        
#         win = sum(nums[:k])
#         maximum = win/k
        
#         for i in range(k , len(nums)):
#             win +=nums[i] - nums[i-k]
#             maximum = max(maximum , win/k)
#         return maximum