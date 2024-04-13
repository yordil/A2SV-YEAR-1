# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i, e in enumerate(height):
            while stack and e >= stack[-1][0]:
                popped, _ = stack.pop()
                if stack:
                    left_border, j = stack[-1]
                   
                    water += min(left_border-popped, e-popped)*(i-j-1)
            stack.append((e,i))
        return water