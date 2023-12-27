class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        
        result = []
        
        left , right = 0 , 0 
        
        while left < len(nums1)  and right < len(nums2):
            if nums1[left] == nums2[right]:
                result.append(nums1[left])
                right+=1
                left+=1
                
            elif nums1[left] > nums2[right]:
                right +=1
            
            else:
                left +=1
                
        return result