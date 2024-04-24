# — coding: utf-8 –

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if not headA or not headB:
        #     return None
        # pa, pb = headA, headB
        # while pa != pb:
        #     if pa is None:
        #         pa = headB
        #     else:
        #         pa = pa.next
        #     if pb is None:
        #         pb = headA
        #     else:
        #         pb = pb.next
        # return pa

        # 我们求出两个链表的长度，并求出两个链表长度的差值，然后让curA移动到，和curB 末尾对齐的位置
        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:         # 求链表B的长度
            cur = cur.next
            lenB += 1
        # 搞俩个头
        curA, curB = headA, headB
        # 交换俩个头，让curB为最长链表的头，lenB为其长度
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        # 让curA和curB在同一起点上（末尾位置对齐）
        for _ in range(lenB - lenA):
            curB = curB.next
        #  遍历curA 和 curB，遇到相同则直接返回
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
