class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def isValid(segment):
            if len(segment) == 0 or len(segment) > 3:
                return False
            if segment[0] == '0' and len(segment) > 1:
                return False
            return 0 <= int(segment) <= 255
        
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                
            for end in range(start + 1, min(len(s) + 1, start + 4)):
                segment = s[start: end]
                if isValid(segment):
                    backtrack(end, path + [segment])
        
        backtrack(0, [])
        return result


            