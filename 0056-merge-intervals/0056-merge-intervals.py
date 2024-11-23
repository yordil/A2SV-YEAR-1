class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key  = lambda x: x[0])

        answer= []

        left = 0

        while left < len(intervals):

            start  , end  = intervals[left]
            tempmax = end
            right = left + 1
            while right < len(intervals) and tempmax >= intervals[right][0]:
                tempmax = max(tempmax , intervals[right][1])
                right +=1
            
            
            if right == left + 1:
                answer.append([start , tempmax])
            else:
                answer.append([start , tempmax])
            
            left = right

        
        return answer