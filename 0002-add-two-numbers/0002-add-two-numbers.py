from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    

# Example usage:
if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")
        result = result.next