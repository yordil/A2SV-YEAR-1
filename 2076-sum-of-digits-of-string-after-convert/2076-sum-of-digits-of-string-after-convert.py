class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        allstring = ""

        for i in s:
            allstring += str(ord(i) - 96)

        while k:
            summ = 0
            for i in allstring:
                summ += int(i)

            allstring = str(summ)
            k-= 1

        return int(allstring)