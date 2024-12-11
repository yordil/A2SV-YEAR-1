class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        
        myhash =  Counter(nums)
        frequency = [ [] for i in range(len(nums) + 1)]

        for num , count in myhash.items():
            frequency[count].append(num)
        
        ans = []

        for i in range(len(frequency) -1 ,  - 1  , -1):
            for num in frequency[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans 

        return 