# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isValid(self, node, k):
        if not node:
            return False
        curr = node
        cnt = 0
        while curr:
            cnt += 1
            if cnt == k:
                return True
            curr = curr.next
        return False
    
    def reverse(self, node):
        curr = node
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevGroupEnd = dummy
        curr = head

        while curr:
            # if fewer than k nodes left, leave
            # the nodes as they are
            if not self.isValid(curr, k):
                break
            
            # find the kth node
            kth = curr
            for i in range(k-1):
                kth = kth.next

            # find the next group first node
            nextGroupNode = kth.next
            # break the group
            kth.next = None
            
            # reverse until kth node
            reversedHead = self.reverse(curr)

            # connect
            prevGroupEnd.next = reversedHead

            curr.next = nextGroupNode

            # move to next group
            prevGroupEnd = curr
            curr = nextGroupNode
        return dummy.next

