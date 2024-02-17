class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans=  0
        if len(s) == 0:
            return 0
        else:
            myhash = { "(" : 0 , ")" : 0}

            for v in s:
                if v == "(":
                    myhash[v] +=1
                else:
                    if myhash["("] > 0:
                        myhash["("] -=1
                    else:
                        ans +=1
            return myhash["("] + ans
