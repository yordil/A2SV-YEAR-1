class HeapItem:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, to_compare):
       
        if self.count == to_compare.count:
            return self.word > to_compare.word  
        return self.count < to_compare.count  

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words) 

        heap = []

        
        for word, count in counts.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heappush(heap, item) 
            else:
                if item > heap[0]: 
                    heappop(heap)  
                    heappush(heap, item) 

        
        result = []
        while heap:
            result.append(heappop(heap).word)

        return result[::-1]  
