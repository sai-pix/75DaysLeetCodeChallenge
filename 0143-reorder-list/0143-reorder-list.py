# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        first,sec=head,prev
        while sec:
            temp1=first.next
            temp2=sec.next
            first.next=sec
            sec.next=temp1
            first=temp1
            sec=temp2