class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) <3:
            return False
        
        n1 = float("inf")
        n2 = float("inf")
        
        for i in range(len(nums)):
            if nums[i] > n2:
                return True
            
            if n1 < nums[i] and nums[i] < n2:
                n2 = nums[i]
            else:
                n1 = min(nums[i] , n1)
                
        
        
#         while k < len(nums):
#             temp1 = nums[i]
#             temp2 = nums[j]3
            
#             if temp1  > temp2:
#                 nums[i] = nums[j]
#                 i+=1
#                 j+=1
#                 continue
                
#             if nums[k] > nums[j]:
#                 return True
            
#             k+=1
                
        return False
                
            
            
        
        
        
        
        
        
#         stack = [nums[0]]
#         for i in range( 1 , len(nums)-1):
            
#             while stack and nums[j] < stack[-1]:
#                 stack.pop()
            
            
#             if stack and stack[-1] >
                
            
            
#             stack = []
#             stack.append(nums[i])
#             for j in range(len(nums)):
#                 if len(stack) == 2  and stack[-1] < nums[j]:
#                     return True
#                 if stack[-1] < nums[j]:
#                     stack.append(nums[j])
#         return False
                    
        