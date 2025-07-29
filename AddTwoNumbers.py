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


def addTwoNumbers(l1, l2):
    carry = 0
    dummy = ListNode()
    current = dummy
    while l1 or l2:
        l1num = l1.val if l1 else 0
        l2num = l2.val if l2 else 0
         
        newVal = (l1num + l2num + carry)%10
        carry  = (l1num + l2num + carry)//10
        
        current.next = ListNode(newVal)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    if carry == 1:
        current.next = ListNode(1)
        
    return dummy.next

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)


printLinkedList(addTwoNumbers(l1, l2))
            
        
    