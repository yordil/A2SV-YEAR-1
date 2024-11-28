class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        short , longer  = nums1 , nums2

        if len(short) > len(longer):

            short , longer  =  nums2   , nums1

        
        l , r   =   0   , len(short)  -  1 
        total_length = len(short) +  len(longer)

        half = total_length // 2

        while True:

            i =  (l + r) // 2
            j = half - i  -  2 


            short_left = short[i]  if i >= 0 else float("-inf")
            short_right = short[i+1] if (i+1) < len(short) else float("inf")
            long_left = longer[j] if j >= 0 else float("-inf")
            long_right = longer[j+1] if (j+1) < len(longer) else float("inf")


            if short_left <= long_right and short_right >= long_left:

                if total_length % 2:
                    return min(short_right , long_right)
                
                max_left = max(long_left , short_left)
                min_right = min(long_right  , short_right)

                median  = (max_left + min_right) / 2

        
                return median

            elif short_right < long_left:
                l = i + 1

            else:
                r  = i - 1

            
            

            

