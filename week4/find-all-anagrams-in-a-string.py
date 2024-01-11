class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        window_size = len(p)
        hashs = defaultdict(int)
        hashp = Counter(p)
        ans = []

        for i in range(len(s)):
            hashs[s[i]] = hashs.get(s[i] , 0) + 1

            if i >= window_size:
                hashs[s[i-window_size]] -= 1
                if hashs[s[i-window_size]] == 0:
                    del hashs[s[i-window_size]]

            if i >= window_size -1 :
                if hashs == dict(hashp):
                    ans.append(i-window_size+1)
                    print(hashs)

            

        return ans
        


