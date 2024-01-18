class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        bookings.sort(key=lambda x : x[0])

        ans = [0] * (n+1)

        for first, last, seats in bookings:
            ans[first] +=seats
            if last != n:
                ans[last+1] -= seats
            
        ans = list(accumulate(ans))
       
        return ans[1:] 

            

