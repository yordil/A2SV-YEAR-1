class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(val , path):
            if sum(path) == n and len(path) == k:
                ans.append(path[:])

            if sum(path) > n:
                return

            for val in range(val , 10):
                path.append(val)
                backtrack(val+1  , path)
                path.pop()
        
        backtrack(1 , path)
        return ans 

