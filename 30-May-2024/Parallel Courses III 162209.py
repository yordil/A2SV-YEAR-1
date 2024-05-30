# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        # finishTime = [(i+1 , time[i]) for i in range(len(time))]

        adjecencylist = defaultdict(list)
     
        indegree = [0]* (n+1)

        for a , b in relations:
            adjecencylist[a].append(b)
            indegree[b] +=1


        myque = deque()
        for i in range(1 , n+1):
            if indegree[i] == 0:
                myque.append((i , time[i-1]))
        
        minumim_month = 0
        timetrack = defaultdict(int)
        while myque:
            maxx = 0
            node , month = myque.popleft()
            timetrack[node] = month
            for nbr in adjecencylist[node]:
                indegree[nbr] -= 1
                timetrack[nbr] = max(month , timetrack[nbr])
                if indegree[nbr] == 0:
                    myque.append((nbr , timetrack[nbr] + time[nbr-1]))
                    timetrack[nbr] += time[nbr-1]
       
        return max(timetrack.values()) if timetrack else max(time)



