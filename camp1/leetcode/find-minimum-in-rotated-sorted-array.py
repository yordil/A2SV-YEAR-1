class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left , right  = 0 , len(nums)-1
        ans = nums[0]
        if len(nums) < 3:
            return min(nums)
        while left <= right:

            midd = (left + right ) // 2
            
            if nums[midd] > ans:
                left =midd + 1 
                # print(55)
            else:
                # print(55)
                right = midd - 1
                ans = min(ans , nums[midd])

        return ans
