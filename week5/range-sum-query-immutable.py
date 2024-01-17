class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.arr = [0] *( len(nums) + 1)
        for i in range(1 ,len(nums)+1):
            self.arr[i] = self.arr[i-1] + nums[i-1]
        print(self.arr)
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.arr[right+1] - self.arr[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)