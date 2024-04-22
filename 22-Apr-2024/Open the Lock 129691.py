# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = deque([('0000', 0)])  
        visited = set(deadends)
        
        while queue:
            current, turns = queue.popleft()
            if current == target:
                return turns
            for i in range(4):
                for move in [-1, 1]:
                    next_digit = (int(current[i]) + move) % 10
                    next_state = current[:i] + str(next_digit) + current[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
        
        return -1  
