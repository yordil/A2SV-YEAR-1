class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        ans = []
        N = len(nums)
        temp = []
        def kSum(k , start , target):

            if k != 2:
                for i in range(start , N - k  +  1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    temp.append(nums[i])
                    kSum(k - 1  , i+1  , target - nums[i])
                    temp.pop()
                return 

            l , r  = start  , N -1

            while l < r:
                curr_sum = nums[l] + nums[r] 

                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l +=1
                else:
                    ans.append(temp  + [nums[l]   , nums [r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        kSum(4 , 0 , target)

        return ans  






            
