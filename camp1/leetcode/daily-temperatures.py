class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(t)
        for i in range(len(t)):
            while stack and t[stack[-1]] < t[i]:
                id = stack.pop()
                ans[id]  = i - id
            stack.append(i)
        return ans




