class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()


        maxx= max(houses[-1] ,  heaters[-1])
        
        minn = -1
    

        def checker(midd):
            o , e = 0 , 0

            while o < len(houses) and e < len(heaters):
                if abs(houses[o] - heaters[e]) > midd:
                    e +=1
                else:
                    o +=1
            if o == len(houses):
                return True
            return False
            
            
                
        # radius
        while minn  + 1 < maxx:

            radius = (minn+maxx) // 2
            val = checker(radius)

            if val:
                maxx = radius
            else:
                minn = radius

        return maxx



        

        # town  = [ [i , 0] for i in houses ]
        # b = [ [i , 1] for i in heaters ]
        # town.extend(b)
        # town.sort(key = lambda x : x[0])
        
