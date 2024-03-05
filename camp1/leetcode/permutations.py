class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =  set()
        ans.add(tuple(nums[::-1]))
        path = deque()
        N = len(nums)
        def backtrack(i , path):
            nonlocal N
            if path and N == len(path) and len(set(path)) == N:
                ans.add(tuple(path.copy()))  
                return  
            if len(path)  > N:
                return 
            x = 0
            for i in range(i , len(nums) * N ):
                path.append(nums[i%N])
                backtrack(i+1 , path)
                x = path.pop()
                  
        backtrack(0 , path)

        return list(ans)