class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3:
            return False
        index = -1
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] > arr[i+1]:
                index = i
                break
        if index == 0:
            return False
        for i in range(index+1 , len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
            
        return True
            
            