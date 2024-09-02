class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        remainder = k % total
        for i in range(len(chalk)):
            if(chalk[i]) > remainder:
                return i
            remainder -= chalk[i]
    