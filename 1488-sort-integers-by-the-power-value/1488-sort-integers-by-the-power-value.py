class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        

        myheap = []

        for i in range(lo , hi+1):

            curr = i
            counter  = 0 
            while curr != 1:

                if curr&1 :
                    curr = 3*curr +  1
                else:
                    curr //= 2
                
                counter +=1

            myheap.append([counter  ,  i])
            
                
        myheap.sort(key = lambda x : x[0])
        
        return myheap[k-1][-1]