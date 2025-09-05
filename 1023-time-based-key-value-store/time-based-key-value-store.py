class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        low, high = 0, len(arr) - 1
        result = ""
        while low <= high:
            mid = (low + high) // 2
            ts, val = arr[mid]
            if ts == timestamp:
                return val
            if ts < timestamp:
                result = val
                low = mid + 1
            else:
                high = mid - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)