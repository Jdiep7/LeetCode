class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None")
    
    
def removeNthFromEnd(head, n):
    current, length, count = head, 0, 0
    while current:
        length += 1
        current = current.next  
       
    prev = head
    newnode = head.next
    if head is None:
        return 
    elif (length - n) == 0:
        head = head.next
        return head
    else:
        while newnode:
            if count == (length-n)-1:
                prev.next = newnode.next
            prev = newnode
            newnode = newnode.next
            count += 1
        return head
    

head = ListNode(1)
head.next = ListNode(2)
'''head.next.next = ListNode(3)
head.next.next.next = ListNode(4)'''

printLinkedList(removeNthFromEnd(head,1))
    