# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # make sure to ask constrain about length of l1 and l2
        curr1 = l1
        curr2 = l2
        head_res = None
        curr_res = None
        carry = 0
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            curr_sum = val1 + val2
            curr_res_val = (curr_sum + carry) % 10
            carry = (curr_sum + carry) // 10
            if not curr_res:
                curr_res = ListNode(curr_res_val)
                head_res = curr_res
            else:
                result_node = ListNode(curr_res_val)
                curr_res.next = result_node
                curr_res = result_node
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry:
            curr_res.next = ListNode(carry)
        return head_res

