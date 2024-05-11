# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

from sortedcontainers import SortedList as sl
class MedianFinder:

    def __init__(self):
        self.num = sl()

    def addNum(self, num: int) -> None:
        self.num.add(num)

    def findMedian(self) -> float:
        if len(self.num) == 1:
            return self.num[0]
        elif len(self.num) % 2 :
            return self.num[len(self.num)//2]
        else:
            return (self.num[len(self.num)//2] + self.num[len(self.num)//2 - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()