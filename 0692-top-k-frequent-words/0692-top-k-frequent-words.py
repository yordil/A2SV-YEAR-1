class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapp = Counter(words)
        heap = []
        for key , value in mapp.items():
            heap.append((-value , key))
        heapify(heap)
        answer = []
        while len(answer) !=k:
            answer.append(heappop(heap)[1])
        return answer