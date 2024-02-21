class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x  : x[1])
        print(points)
        mina  = float("inf")
        maxx  = float("inf")
        ans = 0
        for i in range(len(points)-1 , -1 , -1):
            start , end  = points[i]
            if i == len(points)-1:
                mina = start
                ans = 1
            else:
                if end >= mina:
                    mina  = max(start, mina)
                    continue
                else:
                    ans += 1
                    mina = start
        return ans

        # [[0, 6], [3, 8], [6, 8], [2, 8], [3, 9], [2, 9], [0, 9], [3, 9], [9, 10], [7, 12]]


            
                


