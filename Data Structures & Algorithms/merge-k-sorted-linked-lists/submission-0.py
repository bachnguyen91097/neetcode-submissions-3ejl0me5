# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        current_sorted_LL = lists[0]
        
        def mergeTwoSortedLinkedList(linkedList1, linkedList2):
            curr1 = linkedList1
            curr2 = linkedList2
            dummy = ListNode()
            curr = dummy
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next
            if curr2:
                curr.next = curr2
            if curr1:
                curr.next = curr1
            return dummy.next

        for i in range(1, len(lists)):
            res = mergeTwoSortedLinkedList(current_sorted_LL, lists[i])
            current_sorted_LL = res
        return res
        