class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distlen = len(set(nums))
        count,i = 0 ,0
        myhash = defaultdict(int) #hash map 

        for j in nums: 
            myhash[j] += 1
            while distlen == len(myhash):
                if myhash[nums[i]] == 1 :
                    myhash.pop(nums[i])
                else : 
                    myhash[nums[i]] -= 1
                i += 1
            count += i
        return count