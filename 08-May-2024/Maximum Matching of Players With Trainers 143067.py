# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        answer = 0

        p , t =  len(players)-1 , len(trainers)-1

        while p >= 0 and t >= 0:

            if players[p] > trainers[t]:
                p -= 1
            else:
                answer +=1
                t -=1
                p-=1
        return answer

