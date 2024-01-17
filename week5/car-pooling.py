class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix = 0
        trips.sort(key=lambda x : x[1])
        prefix = [0] * 1001
        for ppl , start , End in trips:
            prefix[start] +=ppl
            prefix[End] -= ppl
        pplsum = 0
        for i in range(1001):
            pplsum += prefix[i]

            if pplsum > capacity:
                return False
        return True 



            






