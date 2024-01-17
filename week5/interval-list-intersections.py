class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        maxx , minn  = max(len(firstList) , len(secondList)) , min(len(firstList) , len(secondList))
        if minn == 0:
            return []

        ans = []

        left = 0
        right = 0
        while left < len(firstList) and right < len(secondList):
            a, b = firstList[left]
            c, d = secondList[right]

            if b >= c and a <= d:
                ans.append([max(a, c), min(b, d)])

            if b < d:
                left += 1
            else:
                right += 1

        return ans


#         for i in range(minn):
           
            

#             if b < c:
#                 ans.append([])
#             else:
                
#             # if b >= c:
#             #     ans.append([])
#             # else:
#             #     ans.append([min(a, c) , max(b , d)])
#         return ans


# # 4 5 2 6
