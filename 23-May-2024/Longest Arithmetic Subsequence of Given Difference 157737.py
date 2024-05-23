# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        myhash = defaultdict(int)
        for val in arr:
            myhash[val] = myhash[val - difference] + 1
        return max(myhash.values()) 
