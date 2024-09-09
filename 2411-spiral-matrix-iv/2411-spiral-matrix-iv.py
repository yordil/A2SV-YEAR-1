# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        

        answer = [[-1] * n for _ in range(m)]
        curr = head
        
    
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        while curr:
           
            for j in range(left, right + 1):
                if curr:
                    answer[top][j] = curr.val
                    curr = curr.next
            top += 1
            
           
            for i in range(top, bottom + 1):
                if curr:
                    answer[i][right] = curr.val
                    curr = curr.next
            right -= 1  
            
           
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if curr:
                        answer[bottom][j] = curr.val
                        curr = curr.next
                bottom -= 1  
            
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if curr:
                        answer[i][left] = curr.val
                        curr = curr.next
                left += 1 
        
        return answer
