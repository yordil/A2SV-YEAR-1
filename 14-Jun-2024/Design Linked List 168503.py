# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

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