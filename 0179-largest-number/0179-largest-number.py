class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = [str(a) for a in nums]
        num.sort(key=lambda x: x * 10, reverse=True)
        result = "".join(num)
        
        result = result.lstrip('0')
        
        return result if result else "0"