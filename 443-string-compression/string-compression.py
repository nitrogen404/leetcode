class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        l = 0
        while l < len(chars):
            r = l
            while r < len(chars) and chars[r] == chars[l]:
                r += 1
            count = r - l
            chars[write] = chars[l]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            l = r
        return write 