# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        if slow.next == None:
            return slow
        else:
            while fast.next:
                slow = slow.next
                fast = fast.next
                if not fast.next:
                    break
                fast = fast.next
            return slow
            
            