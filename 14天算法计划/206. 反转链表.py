# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = head
        nop = head
        if not ans:
            return ans
        while ans.next:
            ans = ans.next
        self.reverse(head)
        # error 需要保证链表无环
        if nop:
            nop.next = None
        return ans
    def reverse(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        # great! wonderful!
        # 递归的理解
        self.reverse(head.next).next = head
        return head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
Solution().reverseList(head)
