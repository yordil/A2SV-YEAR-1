# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a , 2) + int(b , 2))[2:]
        # carry  = 0

        # aa = len(a)-1
        # bb = len(b) -1
        # ans = ""

        # while aa >= 0 and bb >= 0:
        #     ans += a[aa] ^  b [bb] ^ carry
        #     carry = aa[a] & bb[b]
        #     aa- =1
        #     bb -=1

            

        return ans[::-1]
        
