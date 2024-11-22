class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            
            is_sorted = True
            is_consecutive = True
            for j in range(k - 1):
                if subarray[j] >= subarray[j + 1]:
                    is_sorted = False
                if subarray[j + 1] - subarray[j] != 1:
                    is_consecutive = False
                if not (is_sorted and is_consecutive):
                    break
            
            if is_sorted and is_consecutive:
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results
