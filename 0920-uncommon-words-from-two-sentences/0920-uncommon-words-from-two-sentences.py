class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        frequency  = defaultdict(int)

        s1 = s1.split()
        s2 = s2.split()

        for word in s1:
            frequency[word] +=1
        for word in s2:
            frequency[word] +=1
        
        
        return [key for key , val in frequency.items() if val == 1]

    
