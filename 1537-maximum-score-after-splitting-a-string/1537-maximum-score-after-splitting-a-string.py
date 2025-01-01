class Solution:
    def maxScore(self, s: str) -> int:
        count =  0
        s = list(map(int , s))
        print(s)
        prefix = list(accumulate(s))
        zero = 0
        left = 0
        ones  = prefix[-1] - 1 if s[0] == 1 else prefix[-1]
        left = 1 if s[0] == 0 else 0
        maxsum = left + ones
        for i in range(1 , len(s)):
            ones = prefix[-1] - prefix[i-1]
            if i < len(s)-1 and s[i] == 0:
                left +=1
            print(left , ones)
            maxsum = max(maxsum , ones + left)
        return maxsum





