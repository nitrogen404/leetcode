import random 
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return 
        self.map[val] = len(self.values)
        self.values.append(val)
        return True 
    
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        index = self.map[val]
        lastVal = self.values[-1]
        self.values[index] = lastVal
        self.map[lastVal] = index
        self.values.pop()
        del self.map[val]
        return True
        

    def getRandom(self) -> int:
        return self.values[random.randrange(len(self.values))]        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()