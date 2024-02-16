class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        myhash = defaultdict(int)
        # edge case for 0 
        zeros = answers.count(0)
        anss = 0
        for ans in answers:
            if ans == 0:
                anss  += 1
            else:
                if ans not in myhash or myhash[ans] == ans:
                    anss += 1 + ans
                    # reset mfhash
                    myhash[ans] =  0
                else:
                    myhash[ans] +=1
        return anss
        # ans = 0

        # for val in myhash:
        #     if val + 1 >= myhash[val]:
        #         ans += val +1  
        #     elif val != 0:
        #         ans += myhash[val] - (myhash[val] // val +1 )
        
        # return ans + zeros

#  3  3   3  3  3  3  3  3  3  3  
#     3 :  10    3 * 4 = 12  10 - 4 * 2 
# 4 + 4 + 4  = 12  // 
#  1 , 1 , 1 , 1 , 1
#  1 : 5  = 6 expected
#   5 // 1 = 5 * 
#   2 * 3    occurance 