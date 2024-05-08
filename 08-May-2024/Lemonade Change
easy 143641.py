# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [ 0 , 0]
        for b in bills:
            
            if b == 10:
                if arr[0] > 0:
                    arr[0]-=1
                else:
                    return False
            if b == 20:
                if arr[1] > 0:
                    arr[1] -=1
                    if arr[0] > 0:
                        arr[0] -=1
                    else:
                        return False
                elif arr[0] > 2:
                    arr[0] -= 3
                else:
                    return False    
            if b == 5:
                arr[0] +=1
            elif b == 10:
                arr[1] +=1
            # print(arr)
        return True

            
