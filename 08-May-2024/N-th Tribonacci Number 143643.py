# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
          
        if n <= 2:
            return 0 if n==0 else 1
        
        fibb = [0] * (n+1)
        
        fibb[0] = 0 
        fibb[1] = 1
        fibb[2] = 1
        
        for i in range(3 , n+1):
            fibb[i] = fibb[i-1] + fibb[i-2] + fibb[i-3]
            
            
        return fibb[n]
    