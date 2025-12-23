class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        eventSorted = sorted(events, key=lambda x: x[1])
        ends, maxVal = [], []
        for start, end, value in eventSorted:
            if not maxVal:
                maxVal.append(value)
            else:
                maxVal.append(max(maxVal[-1], value))
            ends.append(end)

        events.sort()
        maxTotal = 0
        for start, end, value in events:
            indx = self.binarySearch(ends, start - 1)
            if indx != -1:
                maxTotal = max(maxTotal, value + maxVal[indx])
            else:
                maxTotal = max(maxTotal, value)
        return maxTotal    

    def binarySearch(self, ends, target):
        l, r = 0, len(ends) - 1
        best = -1
        while l <= r:
            mid = (l + r) // 2
            if ends[mid] <= target:
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        return best



