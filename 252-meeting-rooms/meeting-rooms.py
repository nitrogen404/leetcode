class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda intervals: intervals[1])
        for i in range(1, len(intervals)):
            if not (intervals[i][0] >= intervals[i - 1][1] and intervals[i][0] > intervals[i - 1][0]):
                return False
        return True
