from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        
        if endWord not in words:
            return 0
        
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        # O()
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            
            # O(n * 26)
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch == word[i]:
                        continue
                    new_word = word[:i] + ch + word[i + 1: ]
                    if new_word in words and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, steps + 1))
        return 0