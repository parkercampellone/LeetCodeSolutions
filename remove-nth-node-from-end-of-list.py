class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_node = head
        curr_node = head
        prev_node = None
        next_node = None
        length = 1


        # Get the length of the linked list.
        while curr_node.next != None:
            length += 1
            curr_node = curr_node.next

        node_pos_to_remove = length - n 

        curr_node = head

        for i in range(node_pos_to_remove):
            prev_node = curr_node
            curr_node = curr_node.next
            next_node = curr_node.next

        # The for loop was never entered... should mean the root was removed. 
        if prev_node == None and next_node == None:
            head_node = head_node.next
        else:
            prev_node.next = next_node
        
        return head_node
                
        


        
        

