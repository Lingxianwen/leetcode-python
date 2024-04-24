# -*- coding: utf-8 -*-
# @Time : 2023/2/19 16:01
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# 链接：https://leetcode.cn/problems/minimum-size-subarray-sum

# 暴力解法
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 保存 最小长度
        result = 100000
        for i in range(len(nums)):
            minlen = 0
            for j in range(i, len(nums)):
                minlen += nums[j]
                if minlen >= target:
                    sublen = j - i + 1
                    result = result if result < sublen else sublen
                    break
        if result == 100000:
            return 0
        else:
            return result


class Solution2(object):
    def minSubArrayLen2(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 保存 最小长度
        result = 100000
        for i in range(len(nums)):
            minlen = 0
            for j in range(i, len(nums)):
                minlen += nums[j]
                if minlen >= target:
                    sublen = j - i + 1
                    result = result if result < sublen else sublen
                    break
        if result == 100000:
            return 0
        else:
            return result


if __name__ == '__main__':
    sol2 = Solution2()
    a = [2, 3, 1, 2, 4, 3]
    t = 7
    print(sol2.minSubArrayLen2(t, a))
