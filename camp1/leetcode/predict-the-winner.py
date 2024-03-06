class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def calc(l , r ):
            ll, rr = 0 , 0
            if l == r:
                return nums[l]
            
            ll = nums[l] - calc(l+1 , r)
            rr = nums[r] - calc(l , r-1)
            return max(ll ,rr)


        return True  if calc(0 , len(nums)-1) >= 0 else False
