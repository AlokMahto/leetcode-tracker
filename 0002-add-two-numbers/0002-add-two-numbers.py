class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            carry, rem = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry, 10)
            curr.next = curr = ListNode(rem)
            l1 = l1 and l1.next
            l2 = l2 and l2.next

        return dummy.next