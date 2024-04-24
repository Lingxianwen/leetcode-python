# -*- coding: utf-8 -*-
# @Time : 2023/3/22 21:16
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# 输入
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# 输出
# [null, null, null, null, 2, null, 3]
#
# 解释
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
# myLinkedList.get(1);              // 返回 2
# myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
# myLinkedList.get(1);              // 返回 3
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/design-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 单链表
class Node(object):
    def __int__(self, x=0):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0  # 设置一个链表长度的属性，便于后续操作，注意每次增和删的时候都要更新

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 新建新节点，将值置为val
        new_node = Node(val)
        # 头插法
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head
        # 只要链表的next不为空,遍历到最后的位置
        while cur.next:
            cur = cur.next
        # 在最后的位置插入元素 尾插法
        cur.next = new_node
        # 添加成功 链表长度+1
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        在指定位置添加链表元素
        """
        # 如果index<0 选择头插法
        if index < 0:
            self.addAtHead(val)
            return
        # 尾插法
        elif index == self.size:
            self.addAtTail(val)
            return
        # 不存在
        elif index > self.size:
            return

        node = Node(val)
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        node.next = pre.next
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(1)
# myLinkedList.addAtTail(3)
# myLinkedList.addAtIndex(1, 2)  # 链表变为 1->2->3
# myLinkedList.get(1)  # 返回 2
# myLinkedList.deleteAtIndex(1)  # 现在，链表变为 1->3
# myLinkedList.get(1)  # 返回 3
