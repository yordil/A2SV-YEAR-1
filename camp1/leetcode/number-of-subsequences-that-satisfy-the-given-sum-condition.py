class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod =   10 ** 9 + 7
        nums.sort()
        count = 0
        
        for i in range(len(nums)):

            curr = nums[i]

            left , right  = i , len(nums)-1
            ans = -1
            while left <= right:

                midd = (left + right ) // 2

                if curr + nums[midd] > target:
                    right = midd -1 
                else:
                    left = midd + 1
                    ans = max(midd - i , ans)
            
            if ans != -1:
                count += ((2** ans)) % mod 

        return count % mod


