# https://leetcode.cn/problems/binary-search/

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
            mid = int((left+right)/2)
            if target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid+1
            else:
                return mid
        return -1


if __name__ == '__main__':
    sol = Solution()
    a = [2, 7, 9, 13, 15]
    t = 11
    print(sol.search(a, t))
