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
        def dfs(curr, i):
            if i == len(word):
                return curr.is_end
            
            if word[i] == '.':
                for child in curr.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(word[i]) - ord('a')
                child = curr.children[index]
                if not child:
                    return False
                return dfs(child, i + 1)

        return dfs(self.root, 0)
            


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