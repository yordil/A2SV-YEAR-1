class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []

        water =  0

        for i in range(len(height)):
            while stack and height[i] >= stack[-1][0]:
                val , idx  = stack.pop()
                if not stack:
                    break
                
                diff = i -  stack[-1][-1] - 1
                minn = min(stack[-1][0] , height[i]) - val
                curr = diff * minn

                water += curr
            
            
            stack.append([height[i] , i])

        
        return water