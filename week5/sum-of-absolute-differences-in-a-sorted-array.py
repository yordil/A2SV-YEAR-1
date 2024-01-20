class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = list(accumulate(nums))
        total_sum = prefix_sum[-1]
        n = len(nums)
        result = [0] * n

        for i in range(n):
            left_sum = i * nums[i] - (prefix_sum[i - 1] if i > 0 else 0)
            right_sum = (total_sum - prefix_sum[i]) - (nums[i] * (n - 1 - i))
            result[i] = left_sum + right_sum

        return result

