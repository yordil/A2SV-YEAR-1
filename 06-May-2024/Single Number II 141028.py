# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        answer =""
        for i in range(32):
            zeros , ones = 0 , 0
            for val in nums:
                if val & 1<<i:
                    ones +=1
            if ones % 3:
                answer += "1"
            else:
                answer += "0"
        print(answer)
        answ = ""
        ans = int(answer[::-1] , 2) 
        if ans in nums:
            return ans
        else:
            while ans:
                answ += str(1-ans%2)
                ans = ans >> 1
        return -int(answ[::-1] , 2) -1
        
                