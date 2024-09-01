class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        answer = [-1]
        counter  = Counter(barcodes)
        heaped = [ (-val  , key) for key , val in counter.items()]

        heapify(heaped)

    
        while heaped:
            count , num  = heappop(heaped)

            if answer[-1] == num:
                if heaped:
                    c , n = heappop(heaped)
                    answer.append(n)
                    if c+1:
                        heappush(heaped , (c+1 , n))
                
                heappush(heaped , (count , num))
            
            else:
                answer.append(num)

                if count + 1: 
                    heappush(heaped , (count+1 , num))
        
        return answer[1:]