# — coding: utf-8 –
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            # 慢指针一次移动一个，快指针一次移动两个
            slow = slow.next
            fast = fast.next.next
            # 相遇
            if slow == fast:
                index1 = head
                index2 = slow
                while index2 != index1:
                    index1 = index1.next
                    index2 = index2.next
                # 返回相交的指针
                return index1
