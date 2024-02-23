class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack =[] 
        dicti = {}

        for i in range(len(nums2)):

            while stack and stack[-1] < nums2[i]:
                temp = stack.pop()
                dicti[temp] =  nums2[i]
            
            stack.append(nums2[i])
        ans = [-1] * len(nums1)

        for i in range(len(nums1)):
            if nums1[i] in dicti:
                ans[i] = dicti[nums1[i]] 

        return  ans


            