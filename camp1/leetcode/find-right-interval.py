class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            if intervals[0][0] != intervals[0][1]:
                return [-1]
            else:
                return [0]
        N  = len(intervals)
        ans =  [-1] * N
        myhash = { intervals[i][0] : i for i in range(len(intervals))}
        arr = [intervals[i][0] for i in range(len(intervals))]
        print(arr)
        arr.sort()

        def helper(end , i):
            
            left , right   =  0 , len(arr) - 1
            t = float("inf")
            while left <= right:
                midd = (left + right) // 2

                if arr[midd] >= end:
                    right = midd - 1
                    t = min(arr[midd] , t )
                elif arr[midd] < end:
                    left = midd + 1
            if t != float("inf"):
                ans[i] = myhash[t]
                
        for i in range(len(intervals)):
            start, end  = intervals[i]
            helper(end , i)

        return ans
            

                                           

























        # intervals.sort(key = lambda x : x[1])

        # for i in range(1 , len(intervals)):

        #     curr = intervals[i][0]
        #     prev = intervals[i-1][1]

        #     mytup = tuple(intervals[i])
        #     mytupans = tuple(intervals[i-1])

        #     if curr >= prev:
        #         ans[myhash[mytupans]] = myhash[mytup]

        # return ans
















            
        
