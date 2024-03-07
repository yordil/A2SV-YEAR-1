from sortedcontainers import SortedList as sl

class TimeMap:

    def __init__(self):
        self.default = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.default[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        temparr = self.default[key]
        ans  = ""
        left , right = 0 , len(temparr) - 1
        while left <= right:
            midd  = (left + right) // 2
            if temparr[midd][1] <= timestamp  :
                ans = temparr[midd][0]
                left = midd + 1
            else:
                right = midd  - 1
        
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)