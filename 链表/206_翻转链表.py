# 动画演示
# https://pic.leetcode-cn.com/7d8712af4fbb870537607b1dd95d66c248eb178db4319919c32d9304ee85b602-%E8%BF%AD%E4%BB%A3.gif

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个指针，第一个指针叫 pre，最初是指向 null 的。
        pre = None
        # 第二个指针 cur 指向 head，然后不断遍历 cur
        cur = head
        # 每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
        while cur is not None:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre
