# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        counter = 0
        while left  < right:
            left //=2
            right //=2
            print(right , left)
            counter +=1
    
        return left << counter
   