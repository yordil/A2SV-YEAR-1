class Solution:
    def longestPalindrome(self, s: str) -> int:
        myhash = Counter(s)
        ans = 0
        flag = True
        counter = list(myhash.values())
        if len(myhash) == 1:
            return len(s)
    
        counter.sort(key = lambda x : x % 2 == 1 )
        for i in range(len(counter)):
            if i == len(counter) - 1:
                ans += counter[i] 

            elif counter[i] % 2 == 0:
                ans += counter[i]
                
            else:
                ans += counter[i] -1

        return ans



        # print(counter)

        # for hashval in myhash:
        #     if myhash[hashval] % 2 == 0:
        #         ans += myhash[hashval]
        #     elif myhash[hashval] %2 != 0 and myhash[hashval] > 1:
        #         ans += myhash[hashval] -1
        #     if flag and myhash[hashval] == 1:
        #         ans +=1
        #         flag = False
        # return ans
            
