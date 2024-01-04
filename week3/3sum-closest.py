class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        minvalsum = float("inf")
        for i , v in enumerate(nums):
            
            
            left , right = i+1 , len(nums)-1
            
            while left < right:
                
                cursum = (v + nums[left] + nums[right]) 
                if abs(cursum  - target) < abs(minvalsum - target):
                    minvalsum = cursum
                if cursum > target:
                    right -=1
                elif cursum < target:
                    left +=1
                else:
                    return minvalsum
                
        return minvalsum
                