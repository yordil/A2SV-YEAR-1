# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.is_end = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if not cur.children[ord(i) - 97]:
                cur.children[ord(i) - 97] = TrieNode()
            cur = cur.children[ord(i) - 97]
            cur.count +=1
        cur.is_end = True

    def search(self  , word :str ):
        cur = self.root
        leng = len(word)
        count  = 0
        for i in word:
            cur = cur.children[ord(i) - ord("a")] 
            if cur.count and cur.is_end:
                count +=1
             
            
            else:
                return False

        return count
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        answer = []
        maxx = 0
        ans = ""
        for word in words:
            trie.insert(word)

        for word in words:
            val = trie.search(word)
            if val and val > maxx:
                maxx = val
                ans = word
            elif val == maxx:
                ans = min(ans , word)
        
        return ans 

        

        