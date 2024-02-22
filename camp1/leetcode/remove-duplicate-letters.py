class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        myset = set()

        for i in range(len(s)):

            while stack and stack[-1] > s[i] and freq[stack[-1]] > 0 and s[i] not in myset:

                # freq[stack[-1]] -=1
                # if freq[stack[-1]] == 0:
                d = stack.pop()
                myset.discard(d)
                

            if s[i] not in myset:
                stack.append(s[i])
                myset.add(s[i])
            freq[s[i]] -= 1

        return "".join(stack)