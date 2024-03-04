class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add(tuple([]))
        nums.sort()
        def backtrack(i , path):

            ans.add(tuple(path))

            for i in range(i , len(nums)):
                path.append(nums[i])
                backtrack(i+1 , path)
                path.pop()



        backtrack(0 , [])

        return list(ans)