# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree  = [0] * numCourses

        for a , b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        myque = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                myque.append(i)

        visited = set()

        while myque:

            currCourse = myque.popleft()
            visited.add(currCourse)
        
            for nbr in graph[currCourse]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    myque.append(nbr)
                    

        return len(visited) == numCourses