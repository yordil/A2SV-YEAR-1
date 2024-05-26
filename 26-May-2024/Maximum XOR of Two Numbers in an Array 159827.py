# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(2) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if cur.children[int(i)] is None:
                cur.children[int(i)] = TrieNode()
            cur = cur.children[int(i)]
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        obj = Trie()
        arr = []
        for num in nums:
            bit = bin(num)[2:]
            if len(bit) < 32:
                bit = '0' * (32 - len(bit)) + bit
            arr.append(bit)

        for i in arr:
            obj.insert(i)
        
        ans = -1
        for num in arr:
            res = []
            cur = obj.root
            for i in num:
                if i == '0':
                    if  cur.children[1]:
                        cur = cur.children[1] 
                        res.append('1')
                    else:
                        cur = cur.children[0] 
                        res.append('0')

                elif i == '1':
                    if  cur.children[0]:
                        cur = cur.children[0] 
                        res.append('1')
                        
                    else:
                        res.append('0')
                        cur = cur.children[1] 
            ans = max(ans, int("".join(res), 2))

        return ans
