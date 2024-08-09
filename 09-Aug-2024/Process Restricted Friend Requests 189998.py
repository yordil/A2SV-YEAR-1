# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class unionfind:
	def __init__(self, n):
		self.parent = {i: i for i in range(n)}
		self.size = [1] * (n)

	def find(self, x):
		while x != self.parent[x]:
			x = self.parent[x]
			self.parent[x] = self.parent[self.parent[x]]  
		return self.parent[x]

	def union(self, x, y):
		rootx = self.find(x)
		rooty = self.find(y)
		if rootx != rooty:
			if self.size[rootx] < self.size[rooty]:
				self.parent[rootx] = rooty
				self.size[rooty] += self.size[rootx]
			else:
				self.parent[rooty] = rootx
				self.size[rootx] += self.size[rooty]

	def isConnected(self, x, y):
		return self.find(x) == self.find(y)

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        first = unionfind(n)
        second = unionfind(n)

        answer = []
        for a , b in requests:
            first.union(a , b)
            flag = True

            for c , d in restrictions:
                if first.isConnected(c ,d):
                    flag = False
                    break
            if flag:
                second.union(a , b)

            else:
                first = copy.deepcopy(second)
            
            answer.append(flag)
        return answer
