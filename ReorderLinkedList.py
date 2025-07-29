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

def reorderList(head):
  slow, fast = head, head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  second_half = slow.next
  slow.next = None
  prev = None
  current = second_half
  while current:
    temp = current.next
    current.next = prev
    prev = current
    current = temp
  
  
  first = head
  second = prev
  while second:
    first_next = first.next
    second_next = second.next
    
    first.next = second
    second.next = first_next
    
    first = first_next
    second = second_next
    
  return head
    
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(8)

printLinkedList(reorderList(head))
    
    
    
    

        
        
        
        
        




