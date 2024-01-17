class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        Sum = 0
        myhash = {0 : 1}
        counter = 0
       
        for r in range(len(nums)):
            Sum +=nums[r]
            diff  = Sum - k
            if diff in myhash:
                counter += myhash[diff]
            myhash[Sum] = myhash.get(Sum, 0) + 1

        return counter

            