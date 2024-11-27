class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        nums.sort()
        answer = 0

        def binary_search(left , right , target):

            while left <= right:

                midd = left + (right - left) // 2

                if nums[midd] < target:
                    left = midd  + 1
                elif nums[midd] >= target:
                    right = midd -1
            
            return right

        for i in range(N):
            
            low = lower - nums[i]
            up = upper - nums[i]
            

            # left = bisect_left(nums, lower - nums[i], i+1)
            # right = bisect_right(nums, upper - nums[i], i + 1)
            
            
            answer += (binary_search(i+1 , len(nums)-1 , up+1)  -binary_search(i+1 , len(nums)- 1 , low)  )
                
                
       
        return answer
