class Solution:
    def hIndex(self, nums: List[int]) -> int:
        

        left , right  = 0 , len(nums) - 1
        N  = len(nums)
        ans = 0
        midd = 0
        while left <= right:
            midd = (left + right) // 2
            
            if nums[midd] > N - midd:
                right = midd -1 
            elif nums[midd] == N - midd:
                return nums[midd]
            else:
                left = midd + 1
                
        # print(left , right)
        return N - left
            