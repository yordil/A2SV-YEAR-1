# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numberOfNodes = len(edges)

        parentChild = {i : i for i in range(1 , numberOfNodes+1)}

        for parent , child in edges:
            if parentChild[child] == parentChild[parent]:
                return [parent , child]
            else:
                
                parentX = parentChild[child]
                parentY = parentChild[parent]
                if parentX != parentY:
                    for node in parentChild:
                        if parentChild[node] == parentX:
                            parentChild[node] = parentY
        return