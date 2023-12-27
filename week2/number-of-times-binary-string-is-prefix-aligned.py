class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int: 
            prefix = 0
            counter = 0
            cursum = 0
            for i in range(len(flips)):
                prefix += i+1
                cursum += flips[i]
                if prefix == cursum:
                    counter +=1 
            return counter
        
            
    
    
    
    
    
    
#         # def helper():
#         List = [0] * len(flips)
#         prefixsum = [0] * len(flips)
#         count = 0
        
#         j = 0
#         while flips[j] !=1:
#             List[flips[j]-1] = 1
#             j+=1
#         List[flips[j]-1] = 1
#         j+=1
#         k = 0
        
#         if sum(List[:j+1]) == 
#         leftcount = 0
#         # print(List)
        
#         for i in range(j , len(flips)):
#             List[flips[i]-1] = 1
#             if i == j + k:
#                 count+=1
#             k+=1
#         return count
            
            
            