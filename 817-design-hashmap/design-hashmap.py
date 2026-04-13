class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bucket = self.map[index]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))


    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.map[index]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.map[index]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                del bucket[i]
                return 



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)