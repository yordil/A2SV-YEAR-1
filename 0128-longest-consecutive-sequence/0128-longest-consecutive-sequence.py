class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_val = 0
        myset = set(nums)

        for val in myset:
            
            
            count = 0
            if val - 1 not in myset:
                count = 1
                curr = val

                while curr + 1 in myset:
                    curr += 1
                    count += 1

                max_val = max(max_val  , count)

        return max_val
