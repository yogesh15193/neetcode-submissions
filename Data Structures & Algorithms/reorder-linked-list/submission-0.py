# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        prev=None
        current=second
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        second=prev

        l1,l2=head,second
        while l1 and l2:
            next1=l1.next
            next2=l2.next
            l1.next=l2
            l2.next=next1
            l1=next1
            l2=next2



        