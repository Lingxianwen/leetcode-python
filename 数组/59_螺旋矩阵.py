# -*- coding: utf-8 -*-
# @Time : 2023/2/19 19:36
# @Author : 凌贤文
# @Email : lingxw@zjnu.edu.cn

# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]

# 模拟顺时针画矩阵的过程:
# 填充上行从左到右
# 填充右列从上到下
# 填充下行从右到左
# 填充左列从下到上

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0]*n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n//2, n//2   # 迭代的次数。矩阵的中心点
        count = 1

        for offset in range(1,loop+1):
            for i in range(starty, n - offset):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(4))
