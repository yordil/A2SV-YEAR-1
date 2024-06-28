# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        def checker(interval):

            counter = 1
            prev = position[0]

            for i in range(1 , len(position)):

                if position[i] - prev >= interval:
                    prev = position[i]
                    counter +=1
                if counter == m:
                    return True
                
            return  False



        left , right  = 0 , position[-1] - position[0]
        
        answer = 0
        while left <=right:
            interval = (right + left) // 2

            if checker(interval):
                answer = interval
                left = interval + 1
            else:
                right = interval - 1
        return answer
                

