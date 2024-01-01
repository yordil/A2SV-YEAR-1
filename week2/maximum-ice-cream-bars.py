class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count  = 0
        while count < len(costs ) and coins >=0:
           
            coins -= costs[count]
            count+=1

        return count-1 if coins < 0 else count