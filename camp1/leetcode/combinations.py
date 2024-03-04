class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        c =[]
        def backtrack(i , arr):
            nonlocal n 
            if len(arr) == k:
                c.append(arr.copy())
                return c


            for i in range(i , n+1):
                arr.append(i)
                backtrack(i+1 , arr)
                arr.pop()


        backtrack(1 , [] )
        return c 