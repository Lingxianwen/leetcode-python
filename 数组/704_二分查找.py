# https://leetcode.cn/problems/binary-search/

# 这题主要是对数组区间的理解，区间是变化的

# Solution类
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0] or target > nums[len(nums) - 1]:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # 因为当前这个nums[middle]一定不是target，
                # 那么接下来要查找的左区间结束下标位置就是 middle - 1
                right = mid - 1
            elif nums[mid] < target:
                # 当前的mid一定不是target,所以左边的要+1
                left = mid + 1
        return -1


class Solution2:
    def search2(self, nums, target):
        left, right = 0, len(nums)  # 定义target在左闭右开的区间里，即：[left, right)

        while left < right:  # 因为left == right的时候，在[left, right)是无效的空间，所以使用 <
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle  # target 在左区间，在[left, middle)中
            elif nums[middle] < target:
                left = middle + 1  # target 在右区间，在[middle + 1, right)中
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值


if __name__ == '__main__':
    sol = Solution()
    a = [2, 7, 9, 11, 15]
    t = 13
    print(sol.search(a, t))
