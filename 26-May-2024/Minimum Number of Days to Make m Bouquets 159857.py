# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1

        
        maxxday  = max(bloomDay)
        minn =  1
        ans = float("inf")
        while minn <= maxxday:

            middDay = (minn + maxxday) // 2
            counter = 0
            i = 0
            flower = 0
            b = 0
            flag = False
            for i in range(len(bloomDay)):

                if bloomDay[i] <= middDay:
                    flower +=1
                
                else:
                    flower = 0
                
                if flower == k:
                    b+=1
                    flower = 0
                
                if b >= m:
                    flag = True
                    break
            if flag:
                maxxday = middDay - 1
                ans = min(ans , middDay)
            else:
                minn = middDay + 1

        return ans  


