class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        init  = 1

        while target !=1 :

            if target % 2:
                moves +=1
                target -=1
            elif maxDoubles:
                target //=2
                moves+=1
                maxDoubles -=1
            
            if maxDoubles == 0:
                break

        return moves if target==1 else moves + target -1 
        