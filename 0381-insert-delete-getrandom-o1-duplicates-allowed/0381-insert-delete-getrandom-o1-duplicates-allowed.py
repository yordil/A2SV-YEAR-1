class RandomizedCollection: # official solution

    def __init__(self):

        self.lst = []
        self.dict = defaultdict(set) 


    def insert(self, val: int) -> bool:
  
        self.dict[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.dict[val]) == 1


    def remove(self, val: int) -> bool:
       
        if not self.dict[val]:
            return False
        remove_index, last_val = self.dict[val].pop(), self.lst[-1] # pop() on a set
        self.lst[remove_index] = last_val
        self.dict[last_val].add(remove_index)
        self.dict[last_val].discard(len(self.lst) - 1)

        self.lst.pop()
        return True


    def getRandom(self) -> int:
        
        return choice(self.lst)
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()