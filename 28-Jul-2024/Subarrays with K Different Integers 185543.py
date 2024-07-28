# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    
        def atMostK(nums, k):
            count = 0
            left = 0
            myhash = {}

            for right in range(len(nums)):
                myhash[nums[right]] = myhash.get(nums[right], 0) + 1

                while len(myhash) > k:
                    myhash[nums[left]] -= 1

                    if myhash[nums[left]] == 0:
                        del myhash[nums[left]]
                    
                    left += 1

                count += right - left + 1

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)
    #  if you get the approch the question is preety straight forward
    # since finding exactly K elements will be difficult so why don't w ecount at most K and atmost K-1 the difference between these 2 gives us exactly K elements