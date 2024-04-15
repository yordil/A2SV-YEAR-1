# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        stone = [-i for i in stones]
        heapq.heapify(stone)
        i = len(stones)

        while len(stone) > 1:

            last = heapq.heappop(stone)
            prev = heapq.heappop(stone)

            if last == prev:
                continue
            else:
                heapq.heappush(stone , last + (-prev))
        
        return -stone[0] if stone else 0