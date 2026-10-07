class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda intervals: intervals[1])
        prev_end = float('-inf')
        removals = 0
        for i in range(len(intervals)):
            if intervals[i][0] < prev_end:
                removals += 1
            else:
                prev_end = intervals[i][1]
        return removals

