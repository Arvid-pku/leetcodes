# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # error： 需要注意快慢指针的先后行动，退出条件，之类的
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        pre = None
        for i in range(n):
            fast = fast.next
        while fast:
            pre = slow
            fast = fast.next
            slow = slow.next

    # error: 注意首尾的特殊情况
        if pre:
            pre.next = slow.next
            return head
        else:
            return slow.next