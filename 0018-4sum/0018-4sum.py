from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        N = len(nums)   

        for i in range(N - 3):
           
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first = nums[i]

            for j in range(i + 1, N - 2):
             
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                second = nums[j]

                l, r = j + 1, N - 1

                while l < r:
                    currsum = first + second + nums[l] + nums[r]

                    if currsum > target:
                        r -= 1
                    elif currsum < target:
                        l += 1
                    else:
                        ans.append([first, second, nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        

        return ans
