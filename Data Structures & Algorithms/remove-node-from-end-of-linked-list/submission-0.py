# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        current=dummy
        slow,fast=dummy,dummy
        i=0
        while(i<n):
            fast=fast.next
            i=i+1
        # fast is now n steps ahead
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        node_to_be_removed=slow.next
        slow.next=slow.next.next
        return dummy.next
