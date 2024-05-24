# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if not cur.children[ord(i) - 97]:
                cur.children[ord(i) - 97] = TrieNode()
            cur = cur.children[ord(i) - 97]
        cur.is_end = True
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        splited = sentence.split()
        answer = []

        for word in splited:
            curr = trie.root
            tempans = []
            for character in word:
                if curr.is_end:
                    break
                if curr.children[ord(character) - 97]:
                    curr = curr.children[ord(character) - 97]
                    tempans.append(character)
                else:
                    tempans = list(word)
                    break
            if curr.is_end:
                answer.append("".join(tempans))
            else:
                answer.append(word)

        return " ".join(answer)
