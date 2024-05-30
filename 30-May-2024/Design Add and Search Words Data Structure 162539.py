# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if not temp.children[ord(i) - ord("a")]:
                temp.children[ord(i) - ord("a")] = TrieNode()
            temp = temp.children[ord(i) - ord("a")]
        temp.is_end = True
        

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        
        while stack:
            node, i = stack.pop()
            
            if i >= len(word):
                if node.is_end:
                    return True
                
                continue
            
            if word[i] == '.':
                for child in node.children:
                    if child:
                        stack.append((child, i + 1))
            else:
                if node.children[ord(word[i]) - ord('a')]:
                    stack.append((node.children[ord(word[i]) - ord('a')], i + 1))
            


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)