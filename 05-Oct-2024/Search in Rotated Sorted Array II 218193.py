# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # return True if len(nums) == 1 and target in nums else False
        
        left  , right = 0 , len(nums)-1

        final = 0

        ans = float("inf")

        while left <= right:

            midd = (left + right) // 2
            if nums[midd] == target:
                return midd
            if nums[midd] >= nums[0]:
                left = midd+1
            else:
                if ans >= nums[right]:
                    ans = nums[right]
                    final = right
                right = midd-1
        # final = left
        
        def binary(left , right):
            nonlocal target
            while left<= right:
                midd = (left + right) // 2 
                
                if nums[midd] == target:
                    return midd
                elif nums[midd] > target:
                    right -= 1
                else:
                    left +=1
                
            return None

        
        if target == nums[final]:
            return final

        answer = binary(0 , final-1)
        if answer != None: 
            return answer
        else:
            answer = binary(final , len(nums)-1)
            if answer:
                return answer
        
        return False
        
        