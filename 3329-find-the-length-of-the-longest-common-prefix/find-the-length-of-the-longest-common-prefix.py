class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        res = 0
        for num in arr2:
            res = max(res, trie.lengthOfPrefix(num))
        return res

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        curr = self.root
        num = str(num)
        for digit in num:
            if digit not in curr.children:
                curr.children[digit] = TrieNode()
            curr = curr.children[digit]
    def lengthOfPrefix(self, num):
        curr = self.root
        num = str(num)
        res = 0

        for digit in num:
            if digit in curr.children:
                res += 1
                curr = curr.children[digit]
            else:
                break
        return res