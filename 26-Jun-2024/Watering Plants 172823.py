# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        ca = capacity
        counter = 0
        left = 0

        while left < len(plants):

            if ca >= plants[left]:
                ca -= plants[left]
                counter +=1
                left +=1
            else:
                counter += 2*left
                ca =capacity

        return counter

                