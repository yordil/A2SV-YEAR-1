class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        answer = float("-inf")

        left , right  = 0  , len(height) - 1

        while left < right:

            width = right  - left
            minimum_height = min(height[left] , height[right])

            answer  = max(width * minimum_height , answer)

            if height[right] >= height[left]:
                left +=1
            else:
                right -=1

        return answer

