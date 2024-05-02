# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/



class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        myset = set()
        good = float("inf")

        for f, b in zip(fronts, backs):
            if f == b:
                myset.add(f)
            
        for num in (fronts + backs):
            if num not in myset:
                good = min(good, num)
            

        return good if good != float("inf") else 0

                
            
            
  