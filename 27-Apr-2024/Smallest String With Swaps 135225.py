# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, n: str, pairs: List[List[int]]) -> str:
        parent = {i: i for i in range(len(n))}
        size = {i: 0 for i in range(len(n))}
        answer = list(n)
        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        def union(x , y):
            parx = find(x)
            pary = find(y)
            
            if parx != pary:
                if size[parx] > size[pary]:
                    parent[pary] = parx
                    size[parx] += size[pary]
                else:
                    parent[parx] = pary
                    size[pary] += size[parx]
                

        def isConnected(x , y):
            return find(x) == find(y)

        for a , b  in pairs:
            union(a , b)
       
        connected = defaultdict(list)

        for key , vals in parent.items():
            par = find(key)
            if par in connected:
                connected[par].append([key , n[key]])
            else:
                connected[par].append([key , n[key]])
        visited = 0
        for key , val in connected.items():
            myarr = (sorted(val , key = lambda x: x[1]))
            lastptr = len(myarr) - 1
            indexes = [myarr[i][0] for i in range(len(myarr))]
            indexes.sort()
            visited += len(indexes)
            j = 0
            while j <= lastptr:
                idx1 , ch = myarr[j]
                idx2 , ch2 = myarr[lastptr]
                answer[indexes[lastptr]] = ch2
                answer[indexes[j]] = ch
                j+=1
                lastptr-=1
            if visited == len(n):
                break

        return "".join(answer)
        


      



