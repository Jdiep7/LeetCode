class ListNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    
            
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None")

def MergeTwoSortedLikedLists(list1, list2):
    current1, current2 = list1, list2
    head = None
    current = None
    
    while current1 or current2:
        if list1 and (not list2 or list1.val <= list2.val):
            new_node = ListNode(list1.val)
            list1 = list1.next
        elif list2:
            new_node = ListNode(list2.val)
            list2 = list2.next

        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = current.next
    
    return head
        
        
        
        




