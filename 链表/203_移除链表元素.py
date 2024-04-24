# -*- coding: utf-8 -*-
# @Time : 2023/3/6 21:16
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 示例 2：
#
# 输入：head = [], val = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/remove-linked-list-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 添加虚拟节点
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None:
            # 判断要删除的节点
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            return dummy_head.next
