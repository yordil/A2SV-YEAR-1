from collections import deque
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ans = float("inf")
        arr = deque(blocks[:k-1])
        w = arr.count("W")
        # ans = w
        count = 0
        for i in range(k-1 , len(blocks)):
            arr.append(blocks[i])
            a = arr.count("W")
            ans = min(ans , a)
            arr.popleft()
        return ans



        

            
