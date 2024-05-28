# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        myset = set()
        @cache
        def dp(prev , sumed):
            if stones[-1]  ==  sumed:
                return True
            for i in ([prev -1 , prev , prev+1]):
                if i > 0:
                    if sumed  + i in stones:
                        sumedup = sumed + i
                        if dp(i , sumedup):
                            return True
                
            return False

        return dp(0 , 0)


        # if stones[1] - stones[0] > 1:
        #     return False

        # lastval = stones[-1]
        # myhash = defaultdict(set)
        # prev = 1
        # for i in range(1 , len(stones)):
        #     myhash[i].add(prev + 1)
        #     myhash[i].add(prev)
        #     myhash[i].add(prev-1)







        # n = len(stones)
        # i = n -1 
        # prevcurr = -1
        # flag = False

        # while i > 0:
        #     curr = stones[i] - stones[i-1]
        #     idx1 = bisect_left(stones , stones[i] - (curr+1))
        #     idx2 = bisect_left(stones , stones[i] - curr)
        #     if abs(prevcurr - curr)  > 1 and flag:
        #         if abs(prevcurr - (curr+1)) <=1:
        #             i-=2
        #             prevcurr = curr+1
        #             continue
        #         else:
        #             return False
        #     flag = True
        #     i-=1
        #     prevcurr = curr

        # return True


