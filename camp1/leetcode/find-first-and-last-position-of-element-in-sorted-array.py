class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary(l , r , booll): 
            i = -1
            while l <= r:
                mid = (l + r) // 2
                if target  > nums[mid]:
                    l = mid +1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    i = mid 
                    if booll:
                        l = mid + 1
                    else:
                        r = mid - 1

            return i

        l , r  = 0 , len(nums) -1

        left  = binary(l , r , False)
        right = binary(l , r , True)

        return [left , right]