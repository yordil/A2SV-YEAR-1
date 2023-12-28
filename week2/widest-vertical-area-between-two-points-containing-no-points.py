class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        oneD = [p[0] for p in points ]
        oneD.sort()
        maxx = 0
        for  i in range(len(oneD)-1):
            second_point  = oneD[i+1]
            first_point  = oneD[i]            

            maxx = max(maxx , second_point - first_point)
        return maxx
            