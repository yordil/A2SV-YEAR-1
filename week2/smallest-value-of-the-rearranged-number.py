class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num == 0:
            return 0
        if num < 0:
            num *=-1
            n  = list(str(num))
            n.sort(reverse = True)
            # if 0 in n:
            #     i = 0
            #     while n[i] !=0:
            #         i+=1
            #     newlist = n[i:]
            #     ans = n[i] + n[0:i] + n[i:]
            #     return int(str(ans))
            
            return -int("".join(n))
        else:
            n  = list(str(num))
            
            n.sort()
           
            if '0' in n:
                ans = []
                i = 0
                while n[i] =='0':
                    i+=1
                
                ans.append(n[i]) 
                ans.extend(n[0:i])
                ans.extend(n[i+1:])
               
                return int("".join(ans))
            else:
                return int("".join(n))

