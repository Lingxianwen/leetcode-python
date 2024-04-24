# -*- coding: utf-8 -*-
# @Time : 2023/2/18 13:39
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
# 链接：https://leetcode.cn/problems/squares-of-a-sorted-array

# 暴力简单解法：这个时间复杂度是 O(n + nlogn)
# 可以说是O(nlogn)的时间复杂度
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums

# 双指针法
# 数组其实是有序的， 只不过负数平方之后可能成为最大数了。
# 那么数组平方的最大值就在数组的两端，不是最左边就是最右边，不可能是中间。
# 此时可以考虑双指针法了，i指向起始位置，j指向终止位置。
# 定义一个新数组result，和A数组一样的大小，让k指向result数组终止位置。
# 如果nums[i] * nums[i] < nums[j] * nums[j] 那么result[k--] = nums[j] * nums[j];
# 如果nums[i] * nums[i] >= nums[j] * nums[j] 那么result[k--] = nums[i] * nums[i];
# 复杂度为O(n)


class Solution2(object):
    def sortedSquares2(self, nums):
        i = 0
        j = len(nums)-1
        k = len(nums)-1
        result = [0]*len(nums)
        while i <= j:
            # 先取到两边的平分值，因为是最大的数
            left, right = nums[i] ** 2, nums[j] ** 2
            # 然后将大的数放到数组的最后
            if left > right:
                result[k] = left
                i += 1
            else:
                result[k] = right
                j -= 1
            # 不断的将result数组填满
            k -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    a = [-4, -1, 0, 3, 10]
    # print(sol.sortedSquares(a))
    sol2 = Solution2()
    print(sol2.sortedSquares2(a))
