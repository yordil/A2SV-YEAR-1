class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        short , longer  = nums1 , nums2

        if len(short) > len(longer):
            short , longer  = longer , short

        
        l , r = 0  , len(short) -1 

        total_length = len(short) + len(longer)
        half_length = total_length // 2

        while True:

            i  = (l + r) // 2

            j = half_length - i - 2

            short_left = short[i] if i >=  0 else float("-inf")
            longer_left = longer[j] if j >=  0 else float("-inf")
            short_right = short[i+1] if i+1 < len(short) else float("inf")
            longer_right = longer[j+1] if j+1 < len(longer) else float("inf")

            if short_left <= longer_right and short_right >= longer_left:
                if total_length & 1:
                    return min(short_right , longer_right)
                
                else:
                    right_minimum = min(short_right , longer_right)
                    left_maximum = max(short_left , longer_left)

                    return (right_minimum + left_maximum) / 2 

            elif short_left > longer_right:
                
                r = i -1

            else:
                l = i + 1

        