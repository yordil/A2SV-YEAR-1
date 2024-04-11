# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int: 
        def sieve(n):
            arr = [1 for i in range(n+1)]
            arr[0], arr[1] = 0, 0
            p = 2
            while p * p <= n:
                if arr[p]:
                    for i in range(p * p, n+1, p):
                        arr[i] = 0
                p += 1
            ans = []
            for i in range(n+1):
                if arr[i]:
                    ans.append(i)
            return ans

        primes = sieve(n)
        primess = set(primes)
        myhash = defaultdict(int)
        
        def calculate(n):
            j = 0
            myhash.clear()
            while n > 1:
                if j < len(primes) and n % primes[j] == 0:
                    myhash[primes[j]] += 1
                    n /= primes[j]
                else:
                    j += 1
            count  = 0
            for key, val in myhash.items():
                count += (key * val)
            return count
            
        ans = n
        flag = False
        while ans not in primess:
            if n == ans and flag:
                return n 
            flag = True
            ans = calculate(ans)
        return ans 
      
       
        
