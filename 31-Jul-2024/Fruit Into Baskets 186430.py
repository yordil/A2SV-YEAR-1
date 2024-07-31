# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashset = set()
        hashtable = {}

        left = 0
        counter = float("-inf")
        for i in range(len(fruits)):
            hashset.add(fruits[i])
            hashtable[fruits[i]] = hashtable.get(fruits[i] , 0) + 1

            while len(hashtable) > 2:
                hashtable[fruits[left]] -=1 
                if hashtable[fruits[left]] == 0:
                    del hashtable[fruits[left]]
                left+=1
            
            if (i - left)+1 > counter:
                counter = (i - left) + 1
                # print(fruits[left:i+1])
        return counter