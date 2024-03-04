class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans  = []
        lenn = len(nums)
        def backtrack(i , arr):
            ans.append(arr.copy())


            for i in range(i , lenn):
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()

        backtrack(0 , [])

        return ans