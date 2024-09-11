class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        

        end = bin(start ^ goal)[2:]


        return end.count("1")



