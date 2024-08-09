# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        visited   = set()
        mygraph = defaultdict(list)
        indegree = [0] * n

        for i in range(n):
            if leftChild[i] != -1:
                mygraph[i].append(leftChild[i])
                indegree[leftChild[i]] +=1
            if rightChild[i] != -1:
                mygraph[i].append(rightChild[i])
                indegree[rightChild[i]] +=1
        
        myque = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                myque.append(i)
                break
       
        while myque:
            node = myque.popleft()
            visited.add(node)
            
            for nbr in mygraph[node]:
                if nbr not in visited:
                    myque.append(nbr)
                    visited.add(nbr)
                else:
                    return False
    
        return len(visited) == n
