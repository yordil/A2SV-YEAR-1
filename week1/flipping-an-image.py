class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        arr = []
        
        for i, v in enumerate(image):
            cp  = v
            for j in range(len(cp)):
                if cp[j] == 0 :
                    cp[j] = 1
                else:
                    cp[j] = 0
            cp.reverse()
            arr.append(cp)
            
        return arr