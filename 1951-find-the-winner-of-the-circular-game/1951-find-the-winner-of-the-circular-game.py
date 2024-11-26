class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        player = [i+1 for i in range(n)]

        i = 0

        while len(player) > 1:
            i = (i+k -1) % len(player)
            player.pop(i)

        return player[0]
        
        # que = deque([i+1 for i in range(n)])
        # count = 0
        # i = 0
        # while len(que) > 1:
        #     count += 1
        #     if count == k:
        #         que.popleft()
        #         count  = 0
        #     else:
        #         que.append(que.popleft())
            

        # return que[0] 
            
            
        
        