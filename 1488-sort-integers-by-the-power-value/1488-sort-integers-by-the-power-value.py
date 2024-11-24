class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
       
        dp = {1: 0} 

        
        def calc(x):
            if x in dp:
                return dp[x]

            original = x
            steps = 0
            while x != 1 and x not in dp:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                steps += 1

           
            steps += dp.get(x, 0)
            dp[original] = steps
            return steps

        res = []
        for i in range(lo, hi + 1):
            power = calc(i)
            res.append((power, i))  

        
        res.sort()

        return res[k - 1][1]
