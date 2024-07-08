# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr =[]
        arr = []
        myhash = defaultdict(list)
        for i in strs:   
            sortedword = ''.join(sorted(i))
            myhash[sortedword].append(i)
        return list(myhash.values())
            