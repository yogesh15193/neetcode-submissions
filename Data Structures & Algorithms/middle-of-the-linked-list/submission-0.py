# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        length=1
        curr=head
        while curr.next!=None:
            curr=curr.next
            length=length+1
        print(length)
        slow=head
        fast=head
        while fast.next and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        if length %2==0:
            head=slow.next
        else:
            head=slow
        return head
        
        