class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        p = {n: i for i , n in enumerate(arr2)}
        maxx = max(arr2)
        
        def customcomparator(item):
            return p.get(item , item+maxx) 
        
        arr1.sort( key=customcomparator)
        
        return arr1
        

        
        