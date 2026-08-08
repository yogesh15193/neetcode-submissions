# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=1
        l2=1
        curr_A=headA
        curr_B=headB
        while curr_A.next!=None:
            curr_A=curr_A.next
            l1+=1
        while curr_B.next!=None:
            curr_B=curr_B.next
            l2+=1
        print("lengths of l1, l2 are",l1,l2)
        long_l1=False
        long_l2=False
        if l1>l2:
            diff=l1-l2
            long_l1=True
        elif l2>l1:
            diff=l2-l1
            long_l2=True
        else:
            diff=0
        curr_A=headA
        curr_B=headB
        if long_l1:
            for i in range(diff):
                curr_A=curr_A.next
        if long_l2:
            for i in range(diff):
                curr_B=curr_B.next
        while curr_A != None:
            if curr_A == curr_B:
                return curr_A
            curr_A = curr_A.next
            curr_B = curr_B.next 
        return None




        