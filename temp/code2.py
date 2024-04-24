# -*- coding: utf-8 -*-
# @Time : 2022/12/8 21:42
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# Solution类
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(None)
        ans = p
        s = 0
 
        while l1 or l2 or s != 0:
            # S 当l1或者l2为0的时候，S置为1
            s += (l1.val if l1!=None else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            if l1!=None:
                l1 = l1.next
            if l2:
                l2 = l2.next
            s = s // 10
        return ans.next

 
if __name__ == '__main__':
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums,target))
