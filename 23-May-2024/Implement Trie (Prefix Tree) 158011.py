# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        copyroot = self.root
        for character in word:
            diff = ord(character) - 97
            if not copyroot.children[diff]:
                copyroot.children[diff] = TrieNode()
            copyroot = copyroot.children[diff]
        copyroot.is_end  = True

    def search(self, word: str) -> bool:
        copyroot = self.root
        for character in word:
            diff = ord(character) - 97
            if not copyroot.children[diff]:
                return False
            copyroot = copyroot.children[diff]
        return copyroot.is_end
    
            
    def startsWith(self, prefix: str) -> bool:
        copyroot = self.root
        for p in prefix:
            diff = ord(p)  - 97
            if not copyroot.children[diff]:
                return False
            copyroot = copyroot.children[diff]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)