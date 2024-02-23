class Solution:
    def putMarbles(self, we: List[int], k: int) -> int:
        
        arr = [0] * len(we)

        for i in range(1 , len(we)):
            arr[i-1] = we[i] + we[i-1]
        
        arr.sort(reverse=True)

        maxx = sum(arr[:k-1])
        minn = sum(arr[len(we)-k: len(we)])

        return maxx - minn

