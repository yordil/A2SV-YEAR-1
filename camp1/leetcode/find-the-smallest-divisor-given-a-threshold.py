class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        midd = 0
        left  , right  = 1 , max(nums)
        ans = float("inf")
        while left <= right:
            total = 0
            midd = (left + right) // 2

            for num in nums:
                total += ceil(num / midd)
            # print(total)
            if total > threshold:
                left  = midd + 1
            elif total <= threshold :
                right = midd - 1
                ans = min(midd , ans)
            
    
        return ans