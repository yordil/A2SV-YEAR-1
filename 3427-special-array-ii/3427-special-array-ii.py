class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        n = len(nums)
        indicator = [0] * n  
        check = 0
        
    
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:  
                check += 1
            indicator[i] = check
        
        result = []
        for fromi, toi in queries:
            result.append(indicator[fromi] == indicator[toi])
        
        return result
