class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[len(digits) -1 ] != 9:
            digits[len(digits) -1 ] +=1
            return digits
        
        ptr= len(digits)-1
        
        while ptr >= 0:
            if digits[ptr] !=9:
                digits[ptr] +=1
                break
            else:
                digits[ptr] = 0
                ptr -=1
            
        else:
            digits.insert(0 , 1)
            
        return digits
            
            