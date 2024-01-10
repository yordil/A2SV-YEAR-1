class Solution:
        def getAnswer(self, string, k, ch):
            left = 0
            ans = 0
            count = 0
            for i in range(len(string)):
                if string[i] == ch:
                    count += 1
                while count > k:
                    if string[left] == ch:
                        count -= 1
                    left += 1
                ans = max(ans, i - left + 1)
            return ans

        def maxConsecutiveAnswers(self, string, k):
            return max(self.getAnswer(string, k, 'T'), self.getAnswer(string, k, 'F'))