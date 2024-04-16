# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for a in range(len(tasks)):
            tasks[a].append(a)
        tasks.sort(key= lambda x : x[0])
        
        t = tasks[0][0]
        startindex = 0
        answer = []
        heap = []
        

        while startindex < len(tasks) or heap != []:
            while startindex < len(tasks) and t >= tasks[startindex][0]:
                heapq.heappush(heap , [tasks[startindex][1] , tasks[startindex][2]])
                startindex+=1

            if heap:
                tt , idx = heapq.heappop(heap)
                answer.append(idx)
                t += tt
            else:
                t = tasks[startindex][0]
        return answer


        