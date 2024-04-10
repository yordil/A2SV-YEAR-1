# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def bfs():
            que = deque()
            count = 0
            for i in rooms[0]:
                que.append(i)
            visited = set()
            while que:
                index = que.popleft()

                visited.add(index)
                for element in rooms[index]:
                    if element not in visited:
                        que.append(element)
            
                       
            return len(rooms) == len(visited)+1 if 0 not in visited else False


        return bfs()