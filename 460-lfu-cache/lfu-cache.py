class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keytoval = {}
        self.keytofreq = {}
        self.freqtokey = {}
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keytoval:
            return -1

        self._increaseFreq(key)
        return self.keytoval[key]
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.keytoval:
            self.keytoval[key] = value
            self._increaseFreq(key)
            return 
        if len(self.keytoval) >= self.capacity:
            self._evict()

        self.keytoval[key] = value
        self.keytofreq[key] = 1
        
        if 1 not in self.freqtokey:
            self.freqtokey[1] = {}
        
        self.freqtokey[1][key] = None
        self.minFreq = 1
    

    def _increaseFreq(self, key):
        freq = self.keytofreq[key]
        del self.freqtokey[freq][key]

        if not self.freqtokey[freq]:
            del self.freqtokey[freq]
            if self.minFreq == freq:
                self.minFreq += 1
        
        newFreq = freq + 1
        self.keytofreq[key] = newFreq
        if newFreq not in self.freqtokey:
            self.freqtokey[newFreq] = {}
        self.freqtokey[newFreq][key] = None

    def _evict(self):
        evictkey = next(iter(self.freqtokey[self.minFreq]))
        del self.freqtokey[self.minFreq][evictkey]

        if not self.freqtokey[self.minFreq]:
            del self.freqtokey[self.minFreq]

        del self.keytoval[evictkey]
        del self.keytofreq[evictkey]        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)