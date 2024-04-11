# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans  = set()

        path = []

        if sum(candidates) < target:
            return []
        candidates.sort()
        def backtrack(i , path):
            if sum(path) == target:
                ans.add(tuple(path[:]))
                return 
                
            if sum(path)  > target:
                return 
            x = 0
            for i in range(i , len(candidates)):
                if x != candidates[i]:
                    path.append(candidates[i])
                    backtrack(i+1 , path)
                    x = path.pop()

        backtrack(0 , path)
        return list(ans)
