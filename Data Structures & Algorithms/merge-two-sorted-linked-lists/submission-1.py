# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        if not head1:
            return head2
        if not head2:
            return head1
        if not head1 and not head2:
            return 
        head = None
        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        dummy = head
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head = head1
                head1 = head1.next
            else:
                head.next = head2
                head = head2
                head2 = head2.next
        head.next = head1 or head2
        return dummy