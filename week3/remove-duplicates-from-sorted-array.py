class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      
       
        left = 1 
        right = 1
    
        counter=0
        
        while right < len(nums):   
            
            if nums[right-1] != nums[right]:
               
                nums[left] = nums[right] 
                left +=1
           
            right+=1
                
        return left
                
        
       