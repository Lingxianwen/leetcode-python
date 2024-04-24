# -*- coding: utf-8 -*-
# @Time : 2023/2/18 12:12
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# 给你一个数组 nums 和一个值 val，
# 你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。


# 暴力解法：删除一个，然后往后继续移动
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        for i in range(size):
            if nums[i] == val:
                for j in range(i+1, size):
                    nums[j-1] = nums[j]
                i -= 1
                size -= 1
        return size
# python通过不了。很奇怪。

# 暴力解法：直接删除元素
def removeElement2(self, nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


# 双指针解法
class Solution3:
    def removeElement3(self, nums, val):
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    sol = Solution()
    a = [2, 7, 11, 11, 15]
    t = 11
    print(sol.removeElement(a, t))
