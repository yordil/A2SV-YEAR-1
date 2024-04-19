# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        prereq = [0] * num
        mygraph = defaultdict(list)
        for a , b in pre:
            mygraph[b].append(a)
            prereq[a] += 1
        que  = deque()
        for idx , val in enumerate(prereq):
            if val == 0:
                que.append(idx)
        

        answer = []
        def bfs():
            while que:
                node = que.popleft()
                answer.append(node)
                for neighbour in mygraph[node]:
                    prereq[neighbour] -=1
                    if prereq[neighbour] == 0:
                        que.append(neighbour)
            return answer
        aa = bfs()
        return aa if len(aa) == num else []

