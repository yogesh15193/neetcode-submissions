# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr=head
        while curr!=None:
            for i in range(m-1):
                if curr:
                    curr=curr.next
                else:
                    return head

            for j in range(n):
                if curr is None or curr.next is None:
                    return head
                else:
                    curr.next=curr.next.next
            if curr:
                curr=curr.next
        return head
                