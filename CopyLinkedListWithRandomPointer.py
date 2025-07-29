# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None")
    

def copyRandomList(head):
    current = head
    newList = Node(head.val)
    newcur = newList
    while current.next:
        newcur.next = Node(current.next.val)
        newcur = newcur.next
        current = current.next
    printLinkedList(newList)
        
head = Node(3)
head.next = Node(7)
head.next.next = Node(4)
head.next.next.next = Node(5)

copyRandomList(head)