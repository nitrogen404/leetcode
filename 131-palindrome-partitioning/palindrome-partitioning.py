class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(string):
            return string == string[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                prefix = s[start: end]
                if isPalindrome(prefix):
                    path.append(prefix)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result