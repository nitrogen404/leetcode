class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        last_interval = intervals[0]
        result = []
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= last_interval[1]:
                new_interval = [last_interval[0], max(intervals[i][1], last_interval[1])]
                last_interval = new_interval
            else:
                
                result.append(last_interval)
                last_interval = intervals[i]
        result.append(last_interval)
        return result