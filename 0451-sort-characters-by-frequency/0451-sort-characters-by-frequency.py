class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        ans = []
        myheap = []
        for key , val in count.items():
            myheap.append((-val , key))

        heapify(myheap)

        while myheap:
            count , char = heappop(myheap)
            ans.extend([char]* - count)


        return "".join(ans)