class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = deque()
        deck.sort()

        for i in range(len(deck) -1 , -1 , -1):

            if len(answer) < 2:
                answer.appendleft(deck[i])
            else:
                temp = answer.pop()
                answer.appendleft(temp)
                answer.appendleft(deck[i])
        return answer
            