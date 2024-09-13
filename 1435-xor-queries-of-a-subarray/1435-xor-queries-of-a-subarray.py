class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        N = len(arr)

        prefix = [0] * (N+1)

        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        answer = []

        for a , b in queries:
            answer.append(prefix[b+1] ^ prefix[a])

        return answer