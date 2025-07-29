class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def reverseList(head):
    currentNode, prev = head, None
    while currentNode:
        next_node = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = next_node
    
    
    
    return head
        
        
        
        
        




