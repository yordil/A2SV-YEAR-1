class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort(reverse = True)
        Sum = 0
        j = 0
        for i in range(len(processorTime)):
            cursum = processorTime[i] + tasks[j]
            Sum = max(Sum , cursum)
            j+=4
        return Sum
# 10 20
# 1 2 2 3 3 4 5 8