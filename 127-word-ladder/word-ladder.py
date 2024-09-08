class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = wordList.copy()
        words.append(beginWord)

        word_pattern  = defaultdict(list)
        pattern_word = defaultdict(list)

        for word in words:
            for i in range(len(word)):
                word_pattern[word].append(word[:i] + "*" + word[i+1:])
                pattern_word[word[:i] + "*" + word[i+1:]].append(word)
        
        q = deque([beginWord])
        level = 1
        visited = set()

        while q:
            size = len(q)
            level += 1

            for _ in range(size):
                word = q.popleft()
                visited.add(word)

                patterns = word_pattern[word]
                for pattern in patterns:
                    neighbors = pattern_word[pattern]
                    for neighbor in neighbors:
                        if neighbor in visited:
                            continue
                        if neighbor == endWord:
                            return level
                        q.append(neighbor)
            

        return 0
