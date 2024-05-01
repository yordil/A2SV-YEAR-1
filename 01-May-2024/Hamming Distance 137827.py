# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        binx = bin(x)[2:]
        biny = bin(y)[2:]
        
        a = len(binx) -1
        b = len(biny) -1
       
        count = 0
        while a >=0 and b >= 0:
            if binx[a] != biny[b]:
                count +=1 
            a -=1
            b -=1
      
        if a!=-1: 
            count += binx[:a+1].count("1")
           
        else: count += biny[:b+1].count("1")
        return count
