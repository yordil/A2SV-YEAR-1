class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr.sort()

        myhash = defaultdict(int)
    
        for i in range(len(arr)):
            temp = arr[i] % k
            
            diff = k - temp if temp != 0 else 0

            if diff in myhash:
                if myhash[diff] > 1:
                    myhash[diff] -=1
                else:
                    del myhash[diff]
                
               
            else:
                myhash[temp] +=1
           
        return True if len(myhash) == 0 else False

    