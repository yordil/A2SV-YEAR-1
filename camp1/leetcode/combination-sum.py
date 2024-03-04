class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        path = []
        def backtrack(i):
            if sum(path) == target:
                ans.append(path[:])
                return 
            if sum(path) > target:
                return 

            for i in range(i , len(candidates)):
                path.append(candidates[i])
                backtrack(i)
                path.pop()


        backtrack(0)
        return ans