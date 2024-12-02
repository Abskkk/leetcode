class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def check(word, searchWord):
            for i in range(len(searchWord)):
                if len(word) - 1 < i or word[i] != searchWord[i]:
                    return False
            return True
        wordList = sentence.split(' ')
        for i, word in enumerate(wordList):
            if check(word, searchWord):
                return i + 1
        return -1
            