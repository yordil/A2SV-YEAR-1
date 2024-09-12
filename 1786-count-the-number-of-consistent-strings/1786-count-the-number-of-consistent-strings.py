class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        myset = set(allowed)

        count = 0

        for word in words:
            if set(word) - myset == set():
                count+=1

        return count