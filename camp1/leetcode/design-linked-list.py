class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            curnode = self.head
            for _ in range(index):
                curnode = curnode.next
            return curnode.val if curnode else -1    
        return -1

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
        else:
            curnode = self.head
            while curnode.next:
                curnode = curnode.next
            curnode.next = newnode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index <= self.size:
            if index == 0:
                self.addAtHead(val)
            else:
                curnode = self.head
                for _ in range(index - 1):
                    curnode = curnode.next
                newnode = Node(val)
                newnode.next = curnode.next
                curnode.next = newnode
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                curnode = self.head
                for _ in range(index - 1):
                    curnode = curnode.next
                curnode.next = curnode.next.next
            self.size -= 1

# class MyLinkedList:

#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def get(self, index: int) -> int:
#         if self.head and self.size >= index-1:
#             curnode = self.head
          
#             while index:
#                 curnode = curnode.next
#                 index -=1
#             return curnode.val if curnode else -1    
#         return -1
            

#     def addAtHead(self, val: int) -> None:
#         if self.head:
#             headnode = self.head
#             newnode = Node(val)
#             newnode.next = headnode
#         else:
#             self.head = Node(val)
        

#     def addAtTail(self, val: int) -> None:
#         if self.head:
#             curnode= self.head
#             tail = Node(val)
#             while curnode.next:
#                 curnode = curnode.next
#             curnode.next = tail
#         else:
#             self.head = Node(val)
#         self.size +=1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < size+1:
#             curnode = self.head
            
#             while index:
#                 curnode = curnode.next
#                 index-=1
            
#         curnode.next = curnode.next.next

#         self.size +=1

#     def deleteAtIndex(self, index: int) -> None:
#         if index <= self.size
#             curnode = self.head
#             while index:
#                 curnode = curnode.next
#                 index -= 1
#                 if index == 0:
                    
#             self.size -=1



        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # Implementation for Singly Linked List
# class LinkedList:
#     def __init__(self):
#         # Init the list with a 'dummy' node which makes 
#         # removing a node from the beginning of list easier.
#         self.head = ListNode(-1)
#         self.tail = self.head
    
#     def insertEnd(self, val):
#         self.tail.next = ListNode(val)
#         self.tail = self.tail.next

#     def remove(self, index):
#         i = 0
#         curr = self.head
#         while i < index and curr:
#             i += 1
#             curr = curr.next
        
#         # Remove the node ahead of curr
#         if curr:
#             curr.next = curr.next.next

#     def print(self):
#         curr = self.head.next
#         while curr:
#             print(curr.val, ' -> ')
#             curr = curr.next
#         print()