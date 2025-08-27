from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(nums), 0, -1):
            if buckets[freq]:
                for num in buckets[freq]:
                    result.append(num)
                    if len(result) == k:
                        return result
        return result 