class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        maxx= 0 
        for i in range(len(nums)):
            div = ceil(prefix[i] /( i+1) )
            maxx = max(div , maxx )
        return maxx

