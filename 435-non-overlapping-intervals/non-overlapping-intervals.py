class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        removals = 0
        prevEnd = float('-inf')
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                removals += 1
            
        return removals