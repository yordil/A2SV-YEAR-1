# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        frequencywin = defaultdict(int)
        frequencylose = defaultdict(int)

        for a , b in matches:
            frequencywin[a] +=1
            frequencylose[b] +=1
        
        winner  = sorted([key for key, val in frequencywin.items() if key not in frequencylose])
        loser = sorted([key for key , val in frequencylose.items() if val == 1]
)
        return [winner , loser]


