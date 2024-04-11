# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(enum):
            half = len(enum) // 2
            if half:
                left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
                for i in range(len(enum) - 1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        ans[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        
        ans = [0] * len(nums)
        merge_sort(list(enumerate(nums)))
        return ans
