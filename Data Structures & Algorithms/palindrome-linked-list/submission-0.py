# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values=[]
        curr=head
        while curr!=None:
            x=curr.val
            values.append(x)
            curr=curr.next
        print("values",values)
        if values == values[::-1]:
            return True
        else:
            return False
        