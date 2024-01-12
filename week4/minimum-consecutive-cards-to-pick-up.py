class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        if len(set(cards)) == len(cards):
            return -1

        answerleft = 0
        answerright = 0

        left = 0
        right = 0
        ans = float("inf")
        myset= set()

        for i in range(len(cards)):
            if cards[i] not in myset:
                myset.add(cards[i])
            else:
                while left < i and cards[i] in myset:
                    myset.remove(cards[left])
                    left+=1
                myset.add(cards[i])
                
                ans = min(ans , i - left + 2)

            
            
        return ans
            