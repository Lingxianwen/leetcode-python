# — coding: utf-8 –

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 保存链表的长度
        len = 0
        cur = head
        while cur:  # 求链表的长度
            cur = cur.next
            len += 1

        # 添加虚拟节点
        dummy_head = ListNode(next=head)
        cur = dummy_head
        delect = 0
        while cur.next is not None:
            delect += 1
            # 判断要删除的节点
            if delect == len - n:
                cur.next = cur.next.next
            else:
                cur = cur.next
            return dummy_head.next


if __name__ == '__main__':
    sol = Solution()
    head = None
    for i in [4, 3, 2, 1, 0]:
        head = ListNode(i, head)
    t = 2
    print(sol.removeNthFromEnd(head, t))
